# Fake Climate Device

A simple custom integration for Home Assistant, designed for testing installation and update workflows through HACS.

## Version 3.0.0

Version 3 adds automatic integration reload after option changes.

The virtual device contains two sensors:

- Temperature
- Humidity

The sensor values can be configured directly from Home Assistant.

Changes to temperature and humidity are now applied automatically without restarting Home Assistant.

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
2. Go to Custom repositories.
3. Add this repository:
   `https://github.com/marcuandreistefan/ha-fake-climate-device`
4. Select category:
   `Integration`
5. Download Fake Climate Device.
6. Restart Home Assistant after installing or updating the integration.
7. Go to:
   `Settings → Devices & Services → Add Integration`
8. Search for:
   `Fake Climate Device`
9. Add the integration.

## Expected result

The integration creates one virtual device with two entities:

- Temperature sensor
- Humidity sensor

The values can be changed from the integration options.

From version 3.0.0, changing the options automatically reloads the integration, so a full Home Assistant restart is not required just to apply new temperature or humidity values.

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

### v3.0.0

- Automatic integration reload after option changes
- Temperature changes apply without restarting Home Assistant
- Humidity changes apply without restarting Home Assistant
- Development workflow moved to Visual Studio Code + Git + GitHub
- SSH signed commits with GitHub Verified status

## Project roadmap

- V1 — fixed temperature and humidity values
- V2 — configurable values from Home Assistant
- V3 — automatic reload after option changes
- V4 — GitHub release and HACS update workflow test