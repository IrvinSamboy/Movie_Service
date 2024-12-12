from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
        name: str
        plot: str
        genders: List[str]
        casts: List[str]
        
class MovieOut(MovieIn): 
        id: int

class MovieUpdate(MovieIn):
        name: Optional[str] = None
        plot: Optional[str] = None
        genders: Optional[List[str]] = None
        casts: Optional[List[str]] = None
