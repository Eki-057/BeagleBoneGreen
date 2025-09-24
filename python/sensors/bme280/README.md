# BME280 sensor example

This Python script interfaces with a BME280 environmental sensor via the I²C protocol to read and print temperature, humidity, and pressure data continuously.

The BME280 sensor supports atmospheric data acquisition and is widely used in weather stations, IoT applications, and embedded systems.

## Requirements

```bash
sudo apt update
sudo apt install python3-smbus python3-pip python3-bme280 i2c-tools
```

Ensure your BeagleBone Green runs kernel version `6.15.9-bone25` or newer and that the BME280 sensor is connected to the J4 header.
