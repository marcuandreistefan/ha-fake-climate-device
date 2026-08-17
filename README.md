# Fake Climate Device

A simple custom integration for Home Assistant, designed for testing installation and update workflows through HACS.

## Version 2.0.0

Version 2 adds configurable sensor values directly from Home Assistant.

The virtual device still contains two sensors:

- Temperature
- Humidity

But the values are no longer fixed in the code.

## Configuration

After adding the integration, open:

`Settings → Devices & Services → Fake Climate Device`

Then open the integration options and configure:

- Temperature
- Humidity

Default values:

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

## Version history

### v1.0.0

- Fixed temperature: 24 °C
- Fixed humidity: 50 %
- HACS installation test
- Home Assistant device registration

### v2.0.0

- Configurable temperature
- Configurable humidity
- Home Assistant Options Flow
- Sensor values are read from integration options

## Project roadmap

- V1 — fixed temperature and humidity values
- V2 — configurable values from Home Assistant
- V3 — development workflow with Visual Studio Code + Git + GitHub
- V4 — GitHub release and HACS update test

V3 development workflow started with Visual Studio Code.