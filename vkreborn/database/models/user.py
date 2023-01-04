from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    DateTime,
)

from vkreborn.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    muted_until = Column(DateTime, default=None)

    def __repr__(self):
        return f"<User: {self.user_id}>"
