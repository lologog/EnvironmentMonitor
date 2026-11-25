from machine import Pin
from time import sleep
import dht

DHT_PIN = 22
MEASURE_INTERVAL = 2 # [s]

led = Pin("LED", Pin.OUT)

def init_sensor():
    return dht.DHT11(Pin(DHT_PIN))

def read_sensor(sensor):
    sensor.measure()

    temperature = sensor.temperature()
    humidity = sensor.humidity()

    return temperature, humidity

def main():
    sensor = init_sensor()

    while True:
        try:
            led.toggle()

            temperature, humidity = read_sensor(sensor)

            print(f"Temperature: {temperature} C")
            print(f"Humidity: {humidity} %")
        except OSError:
            print("DHT11 error")

        sleep(MEASURE_INTERVAL)

main()