import medoc_api.communicator as communicator
from socket import error as socketError
from threading import Thread
import time
from device_handler2 import DeviceHandler ##uncomment for actual Medoc


# class DeviceHandler(object): ##turn off this class to use actual Medoc
#     #fake DeviceHandler for testing the local server
#     def __init__(self):
#         super().__init__()
#     def ramp_to_target(self, target):
#         print("Setting temperature to ", target)
#     def ramp_to_idle(self):
#         print("Setting temperature to ", 32)
#     def self_test(self):
#         print("Running self-test")
#         time.sleep(5)
#         return True
#     def tsa2_close(self):
#         print("Shutting down Medoc")


device = DeviceHandler()


def execute(connection):
    global device
    funcName, args = connection.get_message(2)
    if funcName == "device.ramp_to_idle":
        connection.close()
        Thread(target = device.ramp_to_idle).run() 
    elif funcName == "device.ramp_to_target":
        connection.close()
        Thread(target = device.ramp_to_target, args = (float(args),)).run()
    elif funcName == "device.self_test":
        connection.send(str(device.self_test()))
        connection.close()
    else:
        connection.close()
        print(funcName, "was not implemented/allowed by server")


def wait_for_input():
    shutdown = False 
    while not shutdown:
        print("Awaiting new connection") #accept connection
        client = communicator.Communicator(sep = "|||")
        print("Client connected")
        while True: #get messages
            try: #i.e., exit, execute
                message = client.get_message()
                if message == "exit":
                    client.close()
                    break
                elif message == "shutdown":
                    shutdown = True
                    client.close()
                    break
                elif message == "execute":
                    execute(client)
            except socketError as e:
                print(e)
                break
    device.tsa2_close()


def do_op():
    wait_for_input()


if __name__ == "__main__":
    device.ramp_to_target(32)
    do_op()