from b0mb3r.services.service import Service


class Finam(Service):
    async def run(self):
        await self.post(
            "https://www.finam.ru/api/smslocker/sendcode",
            data={"phone": "+" + phone},
        )
