from typing import Optional

from sqlalchemy.sql import insert, select, update

from vkreborn.database import engine
from vkreborn.database.models import User


class UserRepository:
    def __init__(self, user_id: int, chat_id: int):
        self.user_id = user_id
        self.chat_id = chat_id

    async def get_user(self) -> User:
        async with engine.connect() as conn:
            query = select(User).where(User.user_id == self.user_id, User.chat_id == self.chat_id)
            user: Optional[User] = (await conn.execute(query)).fetchone()
            return user

    async def add_user(self, is_moder=False):
        async with engine.connect() as conn:
            query = insert(User).values(
                user_id=self.user_id, chat_id=self.chat_id, is_moder=is_moder
            )
            await conn.execute(query)
            await conn.commit()

    async def get_moder_ids(self):
        async with engine.connect() as conn:
            query = select(User.user_id).where(User.chat_id == self.chat_id, User.is_moder)
            moders: User = (await conn.execute(query)).fetchall()
            return [moder[0] for moder in moders]

    async def set_moder(self, value: bool):
        async with engine.connect() as conn:
            user = await self.get_user()
            if not user:
                await self.add_user()

            query = (
                update(User)
                .values(is_moder=value)
                .where(User.user_id == self.user_id, User.chat_id == self.chat_id)
            )
            await conn.execute(query)
            await conn.commit()
