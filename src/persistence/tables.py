from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Uuid, func, text, CheckConstraint, Table, MetaData, Text, TIMESTAMP, DateTime, Enum, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import registry, relationship, deferred, backref
from domain.entities import City
import uuid


metadata_obj = MetaData()
mapper_registry = registry(metadata=metadata_obj)

city_table = Table(
    'entity_city',
    mapper_registry.metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('name', String(length=64), nullable=False, unique=True),
    Column('latitude', Float, nullable=False),
    Column('longitude', Float, nullable=False),
    Column('count', Integer, nullable=False),
    Column("created_date", DateTime, nullable=False),
    Column("updated_date", DateTime, nullable=False)
)

mapper_registry.map_imperatively(
    City,
    city_table,
    properties={
        "created_date": deferred(city_table.c.created_date),
        "updated_date": deferred(city_table.c.updated_date)
    }
)