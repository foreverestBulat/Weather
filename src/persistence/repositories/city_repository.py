from fastapi import Depends
from sqlalchemy import Result, select, update
from domain.entities import City
from persistence.repositories.unit_of_work import UnitOfWork


class CityRepository:
    def __init__(
            self,
            unit_of_work: UnitOfWork = Depends()
        ):
        self.unit_of_work = unit_of_work
        
    async def get_by_name_async(self, name: str):
        result: Result = await self.unit_of_work.database.execute(select(City).where(City.name == name))
        return result.scalars().first()
    
    async def update_count_add_one_async(self, city: str):
        await self.unit_of_work.database.execute(
            update(City)
            .where(City.name == city)
            .values(count=City.count + 1)
            .execution_options(synchronize_session="fetch")
        )
        await self.unit_of_work.database.commit()