from datetime import datetime
from typing import Optional

from sqlalchemy.sql import delete, insert, select, update

from vkreborn.database import engine
from vkreborn.database.models import MutedUser


class MutedUserRepository:
    def __init__(
        self,
        user_id: Optional[int] = None,
        muted_where: Optional[int] = None,
        muted_by: Optional[int] = None,
        muted_until: Optional[datetime] = None,
    ):
        self.user_id = user_id
        self.muted_where = muted_where
        self.muted_by = muted_by
        self.muted_until = muted_until

    async def get(self) -> MutedUser:
        async with engine.connect() as conn:
            query = select(MutedUser).where(MutedUser.user_id == self.user_id)
            user: Optional[MutedUser] = (await conn.execute(query)).fetchone()
            return user

    async def mute(self):
        exists = await self.get()
        if exists:
            await self.update()
        else:
            await self.create()

    async def create(self):
        async with engine.connect() as conn:
            query = insert(MutedUser).values(
                user_id=self.user_id,
                muted_where=self.muted_where,
                muted_by=self.muted_by,
                muted_until=self.muted_until,
            )
            await conn.execute(query)
            await conn.commit()

    async def update(self):
        async with engine.connect() as conn:
            query = (
                update(MutedUser)
                .where(
                    MutedUser.user_id == self.user_id,
                    MutedUser.muted_where == self.muted_where,
                )
                .values(
                    muted_by=self.muted_by,
                    muted_until=self.muted_until,
                )
            )
            await conn.execute(query)
            await conn.commit()

    async def delete(self):
        async with engine.connect() as conn:
            query = delete(MutedUser).where(
                MutedUser.user_id == self.user_id,
                MutedUser.muted_where == self.muted_where,
            )
            await conn.execute(query)
            await conn.commit()

    async def list_by_muted_where(self):
        async with engine.connect() as conn:
            query = select(MutedUser.user_id).where(MutedUser.muted_where == self.muted_where)
            users = (await conn.execute(query)).fetchall()
            return [user[0] for user in users]

    async def list_by_muted_by(self):
        async with engine.connect() as conn:
            query = select(MutedUser.user_id).where(
                MutedUser.muted_where == self.muted_where,
                MutedUser.muted_by == self.muted_by,
            )
            users = (await conn.execute(query)).fetchall()
            return [user[0] for user in users]
