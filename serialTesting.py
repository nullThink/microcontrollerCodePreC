import machine
import time
from RP2040ToESP8266 import *

s = serial_comm(115200)
ipString = '10.245.153.18'

testInput = input("Command?: ")

code = '''
import time
import machine


from secrets import Tufts_Wireless as wifi
import MQTT_CBR as mqtt_CBR

mqtt_broker = '10.245.153.18'
topic_sub = 'test'

topic_pub = 'test'
client_id = 'AntTest'

mqtt_CBR.connect_wifi(wifi)
led = machine.Pin(2, machine.Pin.OUT)  # 6 for 2040

def blink(delay = 0.1):
    led.off()
    time.sleep(delay)

    led.on()
    
def whenCalled(topic, msg):
    print((topic.decode(), msg.decode()))
    blink()
    time.sleep(0.5)
    blink()
        
def main():
    fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
    fred.subscribe(topic_sub)

    old = 0
    i = 0
    while True:
        try:
            fred.check()
            fred.publish(topic_pub,"{0}")
        except OSError as e:
            print(e)
            fred.connect()
        except KeyboardInterrupt as e:
            fred.disconnect()
            print('done')
            break
    
main()
'''.format(testInput)



s.send_code(code)

while True:
    if s.any():
        text = s.readln()
        print(text, end='')
    time.sleep(0.1)