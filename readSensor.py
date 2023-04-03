from machine import Pin, I2C
from time import sleep
import bme280
from dht import DHT22
from machine import ADC


'''Pico OnBoard Temperature'''
onboard_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
'''Barometer BME280'''
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
bme = bme280.BME280(i2c=i2c)
'''DHT22'''
dht22 = DHT22(Pin(15, Pin.IN, Pin.PULL_UP))
'''photoresistor'''
photoresistor = ADC(0)


collection_length = 6
pressure48h = []
onboard_temp48h = []
dht22_temp48h = []
dht22_humi48h = []
photoresistor48h = []

def barometer_bme280():
    temp_bme, pressure_bme, humidity_bme = bme.values[0], bme.values[1].replace("hPa", ""), bme.values[2]
    #print('Temperature: ' + temp_bme + '. Humidity: ' + humidity_bme + '. pressure' + pressure_bme)

    if len(pressure48h) >= collection_length:
        pressure48h.append(pressure_bme)
        pressure48h.pop(0)
    else:
        pressure48h.append(pressure_bme)

def onboardtemp():
    temperature = 27 - ((onboard_temp.read_u16() * conversion_factor) - 0.706)/0.001721
    
    if len(onboard_temp48h) >= collection_length:
        onboard_temp48h.append(temperature)
        onboard_temp48h.pop(0)
    else:
       onboard_temp48h.append(temperature)
       
def read_dht22():
    dht22.measure()
    temperature = dht22.temperature()
    humidity = dht22.humidity()
    
    if len(dht22_temp48h) >= collection_length:
        dht22_temp48h.append(temperature)
        dht22_temp48h.pop(0)
        dht22_humi48h.append(humidity)
        dht22_humi48h.pop(0)
    else:
        dht22_temp48h.append(temperature)
        dht22_humi48h.append(humidity)
       
def read_photoresistor():
    read_resistor = photoresistor.read_u16()
    
    voltage = (65535 - read_resistor) / 65535 * 3.3
    
    if len(photoresistor48h) >= collection_length:
        photoresistor48h.append(voltage)
        photoresistor48h.pop(0)
    else:
       photoresistor48h.append(voltage)
       

while True:
    barometer_bme280()
    onboardtemp()
    read_dht22()
    read_photoresistor()
    
    print(pressure48h)
    print(onboard_temp48h)
    print(dht22_temp48h)
    print(dht22_humi48h)
    print(photoresistor48h)
    
    sleep(3)
        