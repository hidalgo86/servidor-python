import logging
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from app.database.collections import item_collection
from app.database.helpers import item_helper
from app.models.item import ItemSchema, UpdateItemModel

router = APIRouter()

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ruta para obtener todos los documentos de una colección
@router.get("/", response_description="Obtener todos los items")
async def get_items():
    items = []
    async for item in item_collection.find():
        items.append(item_helper(item))
    return items

# Ruta para obtener un documento por su ID
@router.get("/{id}", response_description="Obtener un item por ID")
async def get_item(id: str):
    item = await item_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail=f"Item {id} no encontrado")

# Ruta para crear un nuevo documento
@router.post("/", response_description="Agregar un nuevo item")
async def add_item(item: ItemSchema = Body(...)):
    try:
        item = jsonable_encoder(item)
        new_item = await item_collection.insert_one(item)
        created_item = await item_collection.find_one({"_id": new_item.inserted_id})
        return item_helper(created_item)
    except Exception as e:
        logger.error(f"Error al agregar el item: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

# Ruta para actualizar un documento por su ID
@router.put("/{id}", response_description="Actualizar un item")
async def update_item(id: str, item: UpdateItemModel = Body(...)):
    item = {k: v for k, v in item.dict().items() if v is not None}
    if len(item) >= 1:
        update_result = await item_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": item}
        )
        if update_result.modified_count == 1:
            updated_item = await item_collection.find_one({"_id": ObjectId(id)})
            if updated_item:
                return item_helper(updated_item)
    existing_item = await item_collection.find_one({"_id": ObjectId(id)})
    if existing_item:
        return item_helper(existing_item)
    raise HTTPException(status_code=404, detail=f"Item {id} no encontrado")

# Ruta para eliminar un documento por su ID
@router.delete("/{id}", response_description="Eliminar un item")
async def delete_item(id: str):
    delete_result = await item_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": f"Item {id} eliminado"}
    raise HTTPException(status_code=404, detail=f"Item {id} no encontrado")