This Python script interfaces with a BME280 environmental sensor via the I²C protocol to read and print temperature, humidity, and pressure data continuously.

The BME280 sensor supports atmospheric data acquisition and is widely used in weather stations, IoT applications, and embedded systems.

The libraries that are needed and how to install:

sudo apt update

sudo apt install python3-smbus python3-pip python3-bme280 i2c-tools


Make sure to have the BME280 connected to the J4 port, otherwise it will not work.
