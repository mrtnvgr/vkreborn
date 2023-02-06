from typing import Optional

from sqlalchemy.sql import delete, insert, select

from vkreborn.database import engine
from vkreborn.database.models import DupeChat


class DupeChatRepository:
    def __init__(
        self,
        chat_id: Optional[int] = None,
        group: Optional[str] = None,
    ):
        self.chat_id = chat_id
        self.group = group

    async def add(self):
        async with engine.connect() as conn:
            query = insert(DupeChat).values(chat_id=self.chat_id, group=self.group)
            await conn.execute(query)
            await conn.commit()

    async def delete_from_all_groups(self):
        async with engine.connect() as conn:
            query = delete(DupeChat).where(DupeChat.chat_id == self.chat_id)
            await conn.execute(query)
            await conn.commit()

    async def delete_from_group(self):
        async with engine.connect() as conn:
            query = delete(DupeChat).where(
                DupeChat.chat_id == self.chat_id, DupeChat.group == self.group
            )
            await conn.execute(query)
            await conn.commit()

    async def get_chat_groups(self):
        async with engine.connect() as conn:
            query = select(DupeChat.group).where(DupeChat.chat_id == self.chat_id)
            groups = (await conn.execute(query)).fetchall()
            return [group[0] for group in groups]

    async def get_all_groups(self):
        async with engine.connect() as conn:
            query = select(DupeChat.group)
            groups = (await conn.execute(query)).fetchall()
            return [group[0] for group in groups]

    async def check_group(self):
        groups = await self.get_chat_groups()
        return self.group in groups
