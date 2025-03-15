from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb+srv://hidalgojose86:JsOJUSWEMrrK9BYN@cluster0.es6zp.mongodb.net/"

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.tu_base_de_datos