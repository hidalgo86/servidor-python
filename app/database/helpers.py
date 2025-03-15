from bson.objectid import ObjectId

def item_helper(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
    }