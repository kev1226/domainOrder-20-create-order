from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    user_id: str
    items: List[str]
    total: float
    status: str
