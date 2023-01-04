from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)

from vkreborn.database import Base


class MutedUser(Base):
    __tablename__ = "muted_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    muted_where = Column(Integer, nullable=False)
    muted_by = Column(Integer, nullable=False)
    muted_until = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Muted user: {self.user_id}, chat_id = {self.muted_where}>"
