from medoc_api.tsa_device import TsaDevice
from medoc_api import enums
import logging
import sys
from threading import Thread
import time
if sys.platform == "win32":
    from msvcrt import getch, getche
else:
    from getch import getch, getche


class DeviceHandler:
    def __init__(self): #create device -- will establish a serial connection
        self.device = TsaDevice(auto_connect_port=True) 
        print("Connecting")
        self.device.start_status_thread(0.1)
        print("Initializing and Self-Test")
        self.device.enable_thermode(enums.ThermodeType.DCHEPS)
        self.device.set_active_thermode(enums.ThermodeType.DCHEPS)
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

    def ramp_to_idle(self): #return to baseline temp
        self.device.finite_ramp_by_time(32.0, 1)
        #self.device.finite_ramp_by_temperature(32, 0.1, 0.1, is_stop_on_response_unit_yes=False, time=10000)
        self.device.run_test()

    def ramp_to_target(self, target): #heat up to target temp
        self.device.finite_ramp_by_time(target, 1)
        #self.device.finite_ramp_by_temperature(target, 0.1, 0.1, is_stop_on_response_unit_yes=False, time=10)
        self.device.run_test()

    def self_test(self): #perform Medoc self-test
        set_rest_mode_res = self.device.set_tcu_state(enums.SystemState.RestMode, run_self_test=True, wait_for_state=True)
        if set_rest_mode_res == None:
            print("Failed to send RestMode (SelfTest) request, exiting")
            self.device.finalize()
            return False
        print("Self-Test finished")
        return True

    def tsa2_close(self): #terminate connection to the Medoc
        self.device.end_test()
        self.device.stop_status_thread()
        self.device.finalize()