from sqlalchemy import Boolean, Column, Integer

from vkreborn.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    is_moder = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User: {self.user_id}>, chat_id = {self.chat_id}"
