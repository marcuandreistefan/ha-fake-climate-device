"""Config flow for Fake Climate Device."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback

from .const import (
    CONF_HUMIDITY,
    CONF_TEMPERATURE,
    DEFAULT_HUMIDITY,
    DEFAULT_TEMPERATURE,
    DOMAIN,
)


class FakeClimateConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fake Climate Device."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""

        await self.async_set_unique_id("fake_climate_device_001")
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return self.async_create_entry(
                title="Fake Climate Device",
                data={},
            )

        return self.async_show_form(
            step_id="user",
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Create the options flow."""
        return FakeClimateOptionsFlow()


class FakeClimateOptionsFlow(config_entries.OptionsFlowWithReload):
    """Handle Fake Climate Device options."""

    async def async_step_init(self, user_input=None):
        """Manage the options."""

        if user_input is not None:
            return self.async_create_entry(
                title="",
                data=user_input,
            )

        current_temperature = self.config_entry.options.get(
            CONF_TEMPERATURE,
            DEFAULT_TEMPERATURE,
        )

        current_humidity = self.config_entry.options.get(
            CONF_HUMIDITY,
            DEFAULT_HUMIDITY,
        )

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_TEMPERATURE,
                    default=current_temperature,
                ): vol.Coerce(float),
                vol.Required(
                    CONF_HUMIDITY,
                    default=current_humidity,
                ): vol.Coerce(float),
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
        )
