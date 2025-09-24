# GPIO LED blink

This Python script toggles a GPIO pin on the BeagleBone Green, creating a blinking effect for an LED connected to a specified GPIO line.

It uses the `gpiod` library (`libgpiod`) for low-level GPIO control and is suitable for systems using the newer character device GPIO interface (for example `/dev/gpiochipX`).

## Requirements

```bash
sudo apt-get install python3-libgpiod
```

GPIO line 28 corresponds to header pins P9-1 (ground) and P9-12 (3.3 V) for the LED wiring described in the script.
