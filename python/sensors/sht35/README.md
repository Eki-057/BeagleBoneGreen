# SHT35 temperature and humidity sensor example

This directory contains a Python script for reading a Sensirion SHT35 (or other SHT3x-series) temperature and humidity sensor that is connected to the BeagleBone Green via I²C. The script continuously prints temperature (°C) and relative humidity (%RH) readings to the console and performs CRC checks to validate the data returned by the sensor.

## Hardware setup

- Connect the Grove SHT35 to the BeagleBone Green's I²C bus on header J4 using the Grove cape or jumper wires.
- The example assumes the device is available on `/dev/i2c-2` with address `0x45`. Adjust `I2C_BUS` or `SHT3X_ADDRESS` in `sht35.py` if your wiring uses a different bus or the sensor responds on `0x44`.

## Software requirements

Install the required libraries and enable the I²C interface if you have not already:

```bash
sudo apt update
sudo apt install python3-pip python3-smbus i2c-tools
pip3 install --user smbus2
```

You can verify the sensor is present by running `i2cdetect -y 2` and confirming that the expected address appears in the map.

## Running the example

Execute the script directly to start an interactive readout loop. Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop the program.

```bash
cd ~/BeagleBoneGreen/python/sensors/sht35
python3 sht35.py
```

On each iteration you should see output similar to the following:

```
Temperature: 22.41 °C
Humidity:    47.08 %RH
```

Transient I²C errors and CRC mismatches are reported but the loop continues so the sensor can recover on the next cycle.
