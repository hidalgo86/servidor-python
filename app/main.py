# import os
# import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes.items import router as ItemRouter
from app.routes.cable_diameter import router as CableDiameterRouter

app = FastAPI()

app.include_router(ItemRouter, prefix="/api/items", tags=["Items"])
app.include_router(CableDiameterRouter, prefix="/api/cable-diameter", tags=["Cable Diameter"])

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8000))  # Toma el puerto de Railway si está disponible
#     uvicorn.run(app, host="0.0.0.0", port=port)