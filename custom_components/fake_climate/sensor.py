"""Sensor platform for Fake Climate Device."""

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, UnitOfTemperature
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DEVICE_NAME, DOMAIN, MANUFACTURER, MODEL


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Fake Climate Device sensors."""

    async_add_entities(
        [
            FakeTemperatureSensor(),
            FakeHumiditySensor(),
        ]
    )


class FakeClimateBaseSensor(SensorEntity):
    """Base class for Fake Climate Device sensors."""

    _attr_has_entity_name = True

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""

        return DeviceInfo(
            identifiers={(DOMAIN, "fake_climate_device_001")},
            name=DEVICE_NAME,
            manufacturer=MANUFACTURER,
            model=MODEL,
        )


class FakeTemperatureSensor(FakeClimateBaseSensor):
    """Fake temperature sensor."""

    _attr_name = "Temperature"
    _attr_unique_id = "fake_climate_temperature"
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_value = 24.0


class FakeHumiditySensor(FakeClimateBaseSensor):
    """Fake humidity sensor."""

    _attr_name = "Humidity"
    _attr_unique_id = "fake_climate_humidity"
    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_value = 50.0
