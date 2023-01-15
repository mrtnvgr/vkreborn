from typing import Optional
from sqlalchemy.sql import insert, select, delete
from vkreborn.database import engine
from vkreborn.database.models import WHPicture


class WHPictureRepository:
    def __init__(
        self,
        picture_id: Optional[str | None],
        where_id: Optional[int | None] = None,
        from_id: Optional[int | None] = None,
    ):
        self.picture_id = picture_id
        self.where_id = where_id if int(where_id) > 0 else None
        self.from_id = from_id if int(where_id) < 0 else None

    async def create(self):
        async with engine.connect() as conn:
            query = insert(WHPicture).values(
                picture_id=self.picture_id, where_id=self.where_id, from_id=self.from_id
            )
            await conn.execute(query)
            await conn.commit()

    async def get(self) -> WHPicture:
        async with engine.connect() as conn:
            query = select(WHPicture).where(
                WHPicture.picture_id == self.picture_id,
                WHPicture.where_id == self.where_id,
                WHPicture.from_id == self.from_id,
            )
            user: Optional[WHPicture] = (await conn.execute(query)).fetchall()
            return user

    async def reset_chat(self):
        async with engine.connect() as conn:
            query = delete(WHPicture).where(WHPicture.where_id == self.where_id)
            await conn.execute(query)
            await conn.commit()
