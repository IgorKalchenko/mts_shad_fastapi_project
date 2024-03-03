from pydantic import BaseModel, EmailStr
from typing import List, Optional

from .books import SellerBook

__all__ = ["IncomingSeller", "ReturnedAllSellers", "ReturnedSeller", "ReturnedSellerBooks"]


class BaseSeller(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class IncomingSeller(BaseSeller):
    password: str


class ReturnedSeller(BaseSeller):
    id: int


class ReturnedSellerBooks(ReturnedSeller):
    books: Optional[List[SellerBook]] = []


class ReturnedAllSellers(BaseModel):
    sellers: list[ReturnedSeller]
