from b0mb3r.services.service import Service


class CleverSite(Service):
    async def run(self):
        await self.post(
            "https://clients.cleversite.ru/callback/run.php",
            data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"},
        )
