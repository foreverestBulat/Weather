from math import ceil
from typing import Generic, List, TypeVar

from pydantic import BaseModel


class PaginatedResult(BaseModel):
    current_page: int
    total_pages: int
    total_count: int
    page_size: int
    has_previous_page: bool
    has_next_page: bool
    data: List
    
    @staticmethod
    def create(result, number: int, size: int, total_count: int):
        total_pages = ceil(total_count / size)
        
        return PaginatedResult(
            current_page=number,
            total_count=total_count,
            total_pages=total_pages,
            page_size=size,
            has_next_page=total_pages > number,
            has_previous_page=1 < number,
            data=result
        )
