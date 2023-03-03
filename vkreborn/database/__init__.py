from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from vkreborn.config import SQLALCHEMY_DATABASE_URI


class Base(DeclarativeBase):
    def __init__(self, **kw: Any):
        super().__init__(**kw)


engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
session = AsyncSession(bind=engine)
