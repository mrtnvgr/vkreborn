from typing import Optional

from sqlalchemy.sql import delete, insert, select

from vkreborn.database import engine
from vkreborn.database.models import DupeItem


class DupeItemRepository:
    def __init__(
        self,
        hash: Optional[bytes] = None,
        group: Optional[str] = None,
    ):
        self.hash = hash
        self.group = group

    async def get_item_groups(self):
        async with engine.connect() as conn:
            query = select(DupeItem.group).where(DupeItem.hash == self.hash)
            groups = (await conn.execute(query)).fetchall()
            return [group[0] for group in groups]

    async def get_all_groups(self):
        async with engine.connect() as conn:
            query = select(DupeItem.group)
            groups = (await conn.execute(query)).fetchall()
            return [group[0] for group in groups]

    async def add_to_groups(self, groups: list[str]):
        async with engine.connect() as conn:
            for group in groups:
                query = insert(DupeItem).values(hash=self.hash, group=group)
                await conn.execute(query)
            await conn.commit()

    async def clear_all(self):
        async with engine.connect() as conn:
            query = delete(DupeItem)
            await conn.execute(query)
            await conn.commit()

    async def clear_old(self, chat_groups: list[str]):
        item_groups = await self.get_all_groups()
        groups = [group for group in item_groups if group not in chat_groups]
        async with engine.connect() as conn:
            for group in groups:
                query = delete(DupeItem).where(DupeItem.group == group)
                await conn.execute(query)
            await conn.commit()

    async def clear_group(self):
        async with engine.connect() as conn:
            query = delete(DupeItem).where(DupeItem.group == self.group)
            await conn.execute(query)
            await conn.commit()

    async def delete(self):
        async with engine.connect() as conn:
            query = delete(DupeItem).where(
                DupeItem.group == self.group, DupeItem.hash == self.hash
            )
            await conn.execute(query)
            await conn.commit()
