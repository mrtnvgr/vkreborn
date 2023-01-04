from sqlalchemy import (
    Column,
    Integer,
    Boolean,
)

from vkreborn.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User: {self.user_id}>"
