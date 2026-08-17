"""Config flow for Fake Climate Device."""

from homeassistant import config_entries

from .const import DOMAIN


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
