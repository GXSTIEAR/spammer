from b0mb3r.services.service import Service


class BelTeleCom(Service):
    async def run(self):
        await self.post(
            "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
            data={"phone": phone},
        )
