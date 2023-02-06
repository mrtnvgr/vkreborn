from sqlalchemy import Column, Integer, LargeBinary, String

from vkreborn.database import Base


class DupeChat(Base):
    __tablename__ = "dupe_chats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False)
    group = Column(String, nullable=False)


class DupeItem(Base):
    __tablename__ = "dupe_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(LargeBinary, nullable=False)
    group = Column(String, nullable=False)
