from b0mb3r.services.service import Service


class Lenta(Service):
    async def run(self):
        await self.post(
            "https://lenta.com/api/v1/authentication/requestValidationCode",
            json={"phone": "+" + phone},
        )
