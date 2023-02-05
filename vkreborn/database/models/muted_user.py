from sqlalchemy import Column, DateTime, Integer

from vkreborn.database import Base


class MutedUser(Base):
    __tablename__ = "muted_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    muted_where = Column(Integer, nullable=False)
    muted_by = Column(Integer, nullable=False)
    muted_until = Column(DateTime, nullable=False)
