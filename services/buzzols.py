from b0mb3r.services.service import Service


class Buzzols(Service):
    async def run(self):
        await self.post(
            "https://it.buzzolls.ru:9995/api/v2/auth/register",
            params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"},
        )
