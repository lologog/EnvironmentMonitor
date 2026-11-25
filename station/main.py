from machine import Pin
from time import sleep_ms
import dht

# DHT11 configuration
DHT_PIN = 22
MEASURE_INTERVAL = 2000 # [ms]

# DHT11 API
def init_sensor():
    return dht.DHT11(Pin(DHT_PIN))

def read_sensor(sensor):
    sensor.measure()

    temperature = sensor.temperature()
    humidity = sensor.humidity()

    return temperature, humidity

# Pin setup
led = Pin("LED", Pin.OUT)

# Main application
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

        sleep_ms(MEASURE_INTERVAL)

main()