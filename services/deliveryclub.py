from b0mb3r.services.service import Service


class DeliveryClub(Service):
    async def run(self):
        await self.post(
            "https://www.delivery-club.ru/ajax/user_otp",
            data={"phone": phone},
        )
