from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import numpy as np
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

mpu.configure() # Apply the settings to the registers.

# Create a metric to track time spent and requests made.
REQUEST_MAGNETOMETER = Gauge('sensors_request_magnetometer', 'read magnetic field level from sensors', unit="uT")
REQUEST_TEMPERATURE = Gauge('sensors_request_temperature', 'read temperature level from sensors', unit="C")

# Decorate function with metric.

@REQUEST_MAGNETOMETER.time()
def get_magnetometer(a):
    magnetometer=np.array(a)
    magnetometer=np.absolute(magnetometer)
    magnetometer=np.mean(magnetometer)
    time.sleep(0.5)
    print(magnetometer)

@REQUEST_TEMPERATURE.time()
def get_temperature(b):
    temperature.set(b)
    print(temperature)

#@REQUEST_ACCELEROMETER.set_to_current_time()
#def accelerometer():
#    accelerometer=mpu.readAccelerometerMaster()

#@REQUEST_GYROSCOPE.set_to_current_time()
#def gyroscope():
#    gyroscope=mpu.readGyroscopeMaster()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        get_magnetometer(mpu.readMagnetometerMaster())
        get_temperature(mpu.readTemperatureMaster())
