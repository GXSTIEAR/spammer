from b0mb3r.services.service import Service


class Youla(Service):
    async def run(self):
        await self.post(
            "https://youla.ru/web-api/auth/request_code",
            data={"phone": phone},
        )
