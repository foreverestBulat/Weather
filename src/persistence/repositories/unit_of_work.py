from fastapi import Depends
from sqlalchemy import Result, select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from persistence.database import get_pg_db

class UnitOfWork:
    def __init__(self, db: AsyncSession = Depends(get_pg_db)):
        self.database = db
        
    async def get_by_id_async(self, id, entity_type):
        result: Result = await self.database.execute(select(entity_type).where(entity_type.id == id))
        return result.scalars().first()
    
    async def create_async(self, entity):
        self.database.add(entity)
        await self.database.commit()
        await self.database.refresh(entity)
    
    async def update_async(self, entity):
        self.database.merge(entity)
        await self.database.commit()
        await self.database.refresh(entity)
        
    async def delete_async(self, entity):
        self.database.delete(entity)
        await self.database.commit()
        await self.database.refresh(entity)
