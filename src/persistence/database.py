from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import ASYNC_DB_POSTGRESQL_URL


engine = create_async_engine(url=ASYNC_DB_POSTGRESQL_URL, echo=False)

async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_pg_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()

