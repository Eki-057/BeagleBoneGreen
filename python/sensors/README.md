# Sensor examples

This directory groups together sensor demos that were written for the
BeagleBone Green. Each subfolder focuses on a specific device and
contains a stand-alone script plus detailed instructions.

- `bme280/` – Reads temperature, humidity, and pressure data from a Bosch
  BME280 environmental sensor using the `bme280` helper library.
- `sht35/` – Communicates with a Sensirion SHT35 (SHT3x-series) sensor
  over I²C and includes CRC validation of the returned measurements.

Consult the README in each subdirectory for wiring notes, package
requirements, and example commands.
