from vkbottle.user import Message, UserLabeler

labeler = UserLabeler()


@labeler.message(text="%проверка")
async def test_handler(message: Message):
    await message.answer("Тест!")
