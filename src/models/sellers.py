from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

from .base import BaseModel


class Seller(BaseModel):
    __tablename__ = "sellers_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[int] = mapped_column(String(50), nullable=False)
    books: Mapped[Optional[List["Book"]]] = relationship("Book", backref="seller", cascade="all,delete")
    