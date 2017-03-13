from . import gpio
from . import i2c
from . import camera_driver

def get_gpio_driver():
    return gpio.GPIODriver()

def get_i2c_driver(address, bus=0):
    return i2c.I2CDriver(address, bus)

def get_camera_driver(source):
    return camera_driver.CameraDriver()
