from sqlalchemy import Column, Integer, String

from vkreborn.database import Base


class WHPicture(Base):
    __tablename__ = "wallhaven_pictures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    picture_id = Column(String, nullable=False)
    where_id = Column(Integer)
    from_id = Column(Integer)
