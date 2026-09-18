# Raspberry Pi Pico 2W BadUSB Setup Guide

This guide outlines the essential steps to prepare your Raspberry Pi Pico 2W to run the Linux GRUB password reset and user automation script safely and effectively.

---

## Prerequisites & Requirements

- **Hardware:** Raspberry Pi Pico 2W
- **Firmware:** CircuitPython installed on your Pico 2W
- **Libraries Required:** Adafruit CircuitPython HID bundle

---

## Step 1: Install CircuitPython

If you haven't already flashed CircuitPython onto your Raspberry Pi Pico 2W, follow these instructions:

1. Download the latest **CircuitPython UF2 firmware** for the Raspberry Pi Pico W / 2W from the official [CircuitPython website](https://circuitpython.org/).
2. Press and hold the **BOOTSEL** button on your Pico 2W, then plug it into your computer via a USB cable.
3. Release the button once the Pico appears as a mass storage drive named **RPI-RP2**.
4. Drag and drop the downloaded `.uf2` file onto the drive. The Pico will automatically restart and mount as **CIRCUITPY**.

---

## Step 2: Install Required Libraries

The script relies on Adafruit's HID libraries to simulate keyboard input.

1. Download the latest **CircuitPython Library Bundle** matching your installed major version from the [CircuitPython Library Bundle releases page](https://circuitpython.org/libraries).
2. Extract the downloaded ZIP file.
3. From the `lib` folder inside the bundle, copy the following items and paste them into the `lib` directory on your Pico's **CIRCUITPY** drive:
   - `adafruit_hid` (folder)

---

## Step 3: Deploy the Script

1. Rename your finalized Python script to `code.py`.
2. Copy and paste `code.py` directly into the root directory of your **CIRCUITPY** drive.
3. The Pico will automatically execute the script upon powering up (when plugged into a target machine).

---

## ⚠️ Important Safety & Development Tip

To prevent the Pico from automatically running the script and typing into your own computer every time you plug it in for development or editing:

* **Hardware Kill-Switch (Recommended):** Wire a push button between a designated GPIO pin (e.g., GP15) and GND, and add a check at the very beginning of your `code.py` script to halt execution unless the button is pressed.
