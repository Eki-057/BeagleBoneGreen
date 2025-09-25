# Environmental sensor examples

This directory groups together I²C-based environmental sensor examples for the BeagleBone Green. Each subdirectory contains a dedicated script and README describing the expected wiring and usage instructions.

## BME280 (temperature, humidity, pressure)

`bme280.py` demonstrates how to read data from a Bosch BME280 sensor and print temperature, humidity, and pressure values in a loop.

### Requirements

```bash
sudo apt update
sudo apt install python3-smbus python3-pip python3-bme280 i2c-tools
```

Ensure your BeagleBone Green runs kernel version `6.15.9-bone25` or newer and that the BME280 sensor is connected to the J4 header.

## SHT35 (temperature, humidity)

The `sht35/` folder contains an example that communicates with a Sensirion SHT35 sensor using the `smbus2` library. Refer to [`sht35/README.md`](sht35/README.md) for hardware notes, software dependencies, and execution steps.
