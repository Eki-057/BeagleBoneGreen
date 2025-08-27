import smbus2
import bme280
import time

# Set I2C bus and address
I2C_BUS = 2  # /dev/i2c-2
BME280_ADDRESS = 0x76  # Usually 0x76 or 0x77 depending on wiring

def read_bme280():
    # Open I2C bus
    bus = smbus2.SMBus(I2C_BUS)

    # Load calibration parameters
    bme280_calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)

    # Read data
    bme280_data = bme280.sample(bus, BME280_ADDRESS, bme280_calibration_params)

    return {
        'temperature': bme280_data.temperature,
        'humidity': bme280_data.humidity,
        'pressure': bme280_data.pressure
    }

def main():
    try:
        while True:
            data = read_bme280()
            print(f"Temperature: {data['temperature']:.2f} °C")
            print(f"Humidity: {data['humidity']:.2f} %")
            print(f"Pressure: {data['pressure']:.2f} hPa\n")
            time.sleep(2)  # Delay between readings
    except KeyboardInterrupt:
        print("Measurement stopped by user")

if __name__ == "__main__":
    main()
