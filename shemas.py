from pydantic import BaseModel,Field
from typing import Optional

# пайдентик модель для базы данных
class IphoneSchema(BaseModel):
    id:Optional[int] = Field(default=1)
    name:str = Field(max_length=30, min_length=1)
    battery:int = Field(max_length=100, min_length=60)
    owner:str
