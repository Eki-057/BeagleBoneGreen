# BeagleBoneGreen

This repository contains small experiments and demonstrations for the BeagleBone Green and related hobby projects.  The material is now grouped by language and topic to make it easier to find examples.

## Repository layout

- `python/`
  - `games/` – Console games and exercises originally written for fun while experimenting with Python.
  - `gpio/` – Scripts that exercise the BeagleBone Green GPIO lines using `libgpiod`.
  - `networking/` – Socket programming demos that show how to build TCP clients, servers, and a small chat application.
  - `sensors/` – Drivers and helpers for hardware such as the BME280 and SHT35 environmental sensors.
- `javascript/`
  - `games/` – Browser games created alongside the Python experiments.
  - `usr_led_blink.js` – Example that toggles the on-board USR LED from Node.js.

Each subdirectory contains its own README (when applicable) with instructions for installing dependencies and running the examples.
