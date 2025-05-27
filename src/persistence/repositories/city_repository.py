from fastapi import Depends
from sqlalchemy import Result, func, select, update
from domain.entities import City
from persistence.repositories.unit_of_work import UnitOfWork


class CityRepository:
    def __init__(
            self,
            unit_of_work: UnitOfWork = Depends()
        ):
        self.unit_of_work = unit_of_work
        
    async def get_by_name_async(self, name: str):
        result: Result = await self.unit_of_work.database.execute(
            select(City)
            .where(City.name == name)
        )
        return result.scalars().first()
    
    async def update_count_add_one_async(self, city: str):
        await self.unit_of_work.database.execute(
            update(City)
            .where(City.name == city)
            .values(count=City.count + 1)
            .execution_options(synchronize_session="fetch")
        )
        await self.unit_of_work.database.commit()
        
    async def get_list_by_str_async(self, q, limit=10):
        result: Result = await self.unit_of_work.database.execute(
            select(City.name).
            where(City.name.ilike(f'{q}%')).
            limit(limit)
        )
        return result.scalars().all()
    
    async def get_page_async(self, number, size):
        result = (await self.unit_of_work.database.execute(
            select(City)
            .offset((number - 1) * size)
            .limit(size)
        )).scalars().all()
        
        total = (
            await self.unit_of_work.database.execute(
                select(func.count())
                .select_from(City)
            )
        ).scalar()
        
        return result, total