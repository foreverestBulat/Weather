import datetime
from pathlib import Path
from uuid import UUID, uuid4
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class City:
    id: Optional[UUID] = field(default=None, init=False)
    name: str = None
    latitude: float = None
    longitude: float = None
    count: int = None
    created_date: datetime = field(default_factory=datetime.datetime.utcnow)
    updated_date: datetime = field(default_factory=datetime.datetime.utcnow)
