import socket
import json

class Communicator(object):
    def __init__(self, server=True, host='localhost', port=55250, amount=1024, sep="|"):
        self.server = server
        self.receive_buffer = ""
        self.socket = None
        self.conn = None
        self.client_address = None
        self.host = host
        self.port = port
        self.amount = amount
        self.sep = sep
        if self.server:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.conn,self.client_address = self.socket.accept()
        else:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.connect((self.host, self.port))


    def __del__(self):
        try:
            self.conn.shutdown(1)
        except:
            pass
        if self.server:
            self.socket.close()
        try:
            self.conn.close()
        except:
            pass


    def close(self):
        self.conn.shutdown(1)
        if self.server:
            self.socket.close()
        self.conn.close()


    def send(self,  *messages):
        message = ""
        for m in messages:
            message += str(json.dumps(m)) + self.sep #convert data to string with serialization (json format)
        self.conn.sendall(message.encode('utf8')) #Python3 only permits byte messages, so encode as bytes


    def receive(self):
        buffer = ""
        while self.sep not in buffer:
            r = self.conn.recv(self.amount)
            if 'byte' in str(type(r)): #change bytes to str
                r = r.decode('utf8')
            buffer += r
        return buffer


    def get_message(self, n=1):
        count = 0
        messages = None
        if n > 1:
            messages = tuple()
        while count < n:
            while not self.sep in self.receive_buffer:
                self.receive_buffer += self.receive()
            i = self.receive_buffer.index(self.sep)
            message = json.loads(self.receive_buffer[:i]) #change json str to original type
            self.receive_buffer = self.receive_buffer[i + len(self.sep):] #keep incomplete messages in buffer
            if n == 1:
                return message
            messages += (message,)
            count += 1
        return messages