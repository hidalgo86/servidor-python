from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    description: str

class UpdateItemModel(BaseModel):
    name: str
    description: int
  
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                 "name": "Nombre del item",
                "description": "Descripción del item"
                }
            ]
        }
    }