from connect import connect
import socket
from machine import Pin
import htmlFile
from picoWeather import WeatherStation
from time import sleep

station = WeatherStation()

connect()
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)

s.listen(1)

def host():
    #station.read_barometer_bme280()
    #station.read_onboard_temp()
    station.read_dht22()
    station.read_photoresistor()
        
    html= htmlFile.website(station.dht22_temp, station.dht22_humi, station.photoresistor) # #station.pressure, station.onboard_temp
    client, addr = s.accept()
    request = str(client.recv(1024))
    client.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n" + html)
    client.close()

try:
    while True:
        try:
            host()
        except OSError:
            print(OSError)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
