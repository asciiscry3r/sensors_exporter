from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import numpy as np
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import RPi.GPIO as GPIO


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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print(GPIO.RPI_INFO)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(29, GPIO.LOW)

# Create a metric to track time spent and requests made.
request_magnetomer = Gauge('sensors_request_magnetometer', 'read magnetic field level from sensors', unit="uT")
request_temperature = Gauge('sensors_request_temperature', 'read temperature level from sensors', unit="C")

# Decorate function with metric.

def get_magnetometer(a):
    magnetometer=np.array(a)
    magnetometer=np.absolute(magnetometer)
    magnetometer=np.mean(magnetometer)
    return magnetometer

#def accelerometer():
#    accelerometer=mpu.readAccelerometerMaster()

#def gyroscope():
#    gyroscope=mpu.readGyroscopeMaster()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000    # Generate some requests.
    while True:

        current_field = get_magnetometer(mpu.readMagnetometerMaster())
        alert_level = 60

        if current_field >= alert_level:
            GPIO.output(29, GPIO.HIGH)
            GPIO.output(29, GPIO.LOW)

        request_magnetomer.set(get_magnetometer(mpu.readMagnetometerMaster())
        request_temperature.set(mpu.readTemperatureMaster())
