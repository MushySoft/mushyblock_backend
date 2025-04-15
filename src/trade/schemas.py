from pydantic import BaseModel
from enum import Enum
from typing import Optional


class OfferType(Enum):
    item = "item"
    service = "service"

    def __str__(self):
        return f"{self.item}, {self.service}"


class OfferCreate(BaseModel):
    id_trade: int
    title: str
    type: OfferType # item или service
    title: str
    description: str
    count: Optional[int] = None # для service = None
    price: int
    photo: Optional[str] = None # запросить файл формата jpg/png (будет реализовано позже)
