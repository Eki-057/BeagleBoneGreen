# BME280 environmental sensor example

This folder contains a Python script that reads temperature, humidity,
and pressure data from a Bosch BME280 sensor connected to the
BeagleBone Green via I²C.

## Requirements

```bash
sudo apt update
sudo apt install python3-smbus python3-pip python3-bme280 i2c-tools
```

## Running the example

1. Connect the BME280 to the `/dev/i2c-2` bus on the BeagleBone Green
   (typically header J4) and confirm the device appears with
   `i2cdetect -y 2`.
2. From this directory, run the script:

   ```bash
   cd ~/BeagleBoneGreen/python/sensors/bme280
   python3 bme280.py
   ```

The script prints the measured values every few seconds until you press
<kbd>Ctrl</kbd>+<kbd>C</kbd>.
