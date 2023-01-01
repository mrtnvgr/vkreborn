from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()


@labeler.message(text="%проверка")
async def test_handler(message: Message):
    await message.answer("Тест!")
