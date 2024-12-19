from pydantic import BaseModel,Field


# пайдентик модель для базы данных
class IphoneSchema(BaseModel):
    id:int = Field(default=1)
    name:str = Field(max_length=30, min_length=1)
    battery:int = Field(le=60,ge=100)
    owner:str
