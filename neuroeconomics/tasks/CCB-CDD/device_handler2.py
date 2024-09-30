from medoc_api.tsa_device import TsaDevice
from medoc_api import enums
import logging
import sys
from threading import Thread
import time
##from multiprocessing import Process
##from concurrent.futures import ThreadPoolExecutor
if sys.platform == "win32":
    from msvcrt import getch, getche
else:
    from getch import getch, getche


class DeviceHandler:
    def __init__(self):
        self.device = TsaDevice(auto_connect_port=True) #create device. It will establish a serial connection
        print("Connecting")
        self.device.start_status_thread(0.1)
        print("Initializing and Self-Test")
        self.device.enable_thermode(enums.ThermodeType.DCHEPS)
        self.device.set_active_thermode(enums.ThermodeType.DCHEPS)
        #self.device.set_tcu_state(enums.SystemState.TestInit, run_self_test=False, wait_for_state=True)

        set_rest_mode_res = self.device.set_tcu_state(enums.SystemState.RestMode, run_self_test=True, wait_for_state=True)
        i = 0
        while set_rest_mode_res is None and i < 3:
            set_rest_mode_res = self.device.set_tcu_state(enums.SystemState.RestMode, run_self_test=True, wait_for_state=True)
            i += 1
        if set_rest_mode_res is None:
            print("Failed to send RestMode (SelfTest) request, exiting")
            self.device.finalize()
            exit()
        print("Self-Test finished")
        print("Going into TestInit mode")
        self.device.set_tcu_state(enums.SystemState.TestInit, run_self_test=True, wait_for_state=True)

        

    def ramp_to_idle(self): #function to return to baseline temp
        self.device.finite_ramp_by_time(32.0, 1)
        #self.device.finite_ramp_by_temperature(32, 0.1, 0.1, is_stop_on_response_unit_yes=False, time=10000)
        self.device.run_test()


    def ramp_to_target(self, target): #function to heat up to target temp
        #self.device.set_tcu_state(enums.SystemState.TestInit, run_self_test=False, wait_for_state=True)
        #self.device.finite_ramp_by_time(target, 1)
        self.device.finite_ramp_by_temperature(target, 0.1, 0.1, is_stop_on_response_unit_yes=False, time=10)
        self.device.run_test()


    def self_test(self): #function to perform Medoc self-test
        set_rest_mode_res = self.device.set_tcu_state(enums.SystemState.RestMode, run_self_test=True, wait_for_state=True)
        if set_rest_mode_res == None:
            print("Failed to send RestMode (SelfTest) request, exiting")
            self.device.finalize()
            return False
        print("Self-Test finished")
        return True


    def cool_down(device):
        device.end_test()
        device.stop_status_thread()
        device.finalize()
        core.quit()


    def tsa2_close(self):
        self.device.end_test()
        self.device.stop_status_thread()
        self.device.finalize()


####unsuccessful attempts to assign thread for Medoc####
    #def _ramp_to_target(self, target):
    #    self.device.set_tcu_state(enums.SystemState.TestInit, run_self_test=False, wait_for_state=True)
    #    self.device.finite_ramp_by_temperature(target, 0.1, 0.1, is_stop_on_response_unit_yes=False, time=10000)
    #    self.device.run_test()


    #def ramp_to_target(self, target):
    #    with ThreadPoolExecutor(max_workers = 1) as executor:
    #        executor.submit(self._ramp_to_target, target)
    #    t = Process(target = self._ramp_to_target, kwargs = dict(target = target))
    #    t = Thread(target = self._ramp_to_target, kwargs = dict(target = target))
    #    t.start()
    #    t.join()