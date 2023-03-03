from vkreborn.database import engine
from vkreborn.database.models import User


async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
