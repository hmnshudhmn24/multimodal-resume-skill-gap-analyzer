from pydantic import BaseModel
from typing import List
class Roadmap(BaseModel): skills:List[str]
