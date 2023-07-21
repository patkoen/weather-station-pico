import network
import time
import rp2

ssid = ""
password = ""

def connect():
    rp2.country("AT")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
     
    while not wlan.isconnected() and wlan.status() >= 0:
        print("Auf Verbindung warten...")
        time.sleep(1)

    print(wlan.ifconfig())
    return wlan

if __name__ == "__main__":
    wlan = connect()
