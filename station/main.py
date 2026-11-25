from machine import Pin
from time import sleep_ms
import dht

# DHT11 configuration
DHT11_MEAS_PIN = 22

# DHT11 API
def init_dht11_sensor():
    return dht.DHT11(Pin(DHT11_MEAS_PIN))

def read_dht11_sensor(sensor):
    sensor.measure()

    temperature = sensor.temperature()
    humidity = sensor.humidity()

    return temperature, humidity

# Pin setup
led = Pin("LED", Pin.OUT)

# Main application
def main():
    sensor = init_dht11_sensor()

    while True:
        try:
            led.toggle()

            temperature, humidity = read_dht11_sensor(sensor)

            print(f"Temperature: {temperature} C")
            print(f"Humidity: {humidity} %")
        except OSError:
            print("DHT11 error")

        sleep_ms(2000)

main()