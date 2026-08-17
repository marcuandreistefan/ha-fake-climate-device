# Fake Climate Device

A simple custom integration for Home Assistant, designed for testing installation and update workflows through HACS.

## Version 1.0.0

This first version creates one virtual device with two fixed-value sensors:

- Temperature: 24 °C
- Humidity: 50 %

## Device information

- Manufacturer: Marcu Test Lab
- Model: Virtual TH Sensor
- Integration domain: `fake_climate`

## Installation with HACS

1. Open HACS in Home Assistant.
2. Go to custom repositories.
3. Add this repository:
   `https://github.com/marcuandreistefan/ha-fake-climate-device`
4. Select category:
   `Integration`
5. Download Fake Climate Device.
6. Restart Home Assistant.
7. Go to:
   `Settings → Devices & Services → Add Integration`
8. Search for:
   `Fake Climate Device`
9. Add the integration.

## Expected result

Home Assistant should create one device:

`Fake Climate Device`

with two entities:

- Temperature — 24 °C
- Humidity — 50 %

## Project roadmap

- V1 — fixed temperature and humidity values
- V2 — configurable values from Home Assistant
- V3 — dynamically changing simulated values
- V4 — GitHub release and HACS update test
