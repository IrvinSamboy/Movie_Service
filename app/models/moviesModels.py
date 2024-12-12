from pydantic import BaseModel
from typing import List

class Movies(BaseModel):
        name: str
        plot: str
        genders: List[str]
        casts: List[str]