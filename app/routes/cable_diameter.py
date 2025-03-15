import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.cable_diameter import CableCalculationRequest

router = APIRouter()

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ruta para calcular el diámetro del cable
@router.post("/calculate", response_description="Calcular el diámetro del cable", response_model=dict)
async def calculate_cable_diameter(request: CableCalculationRequest):
    """
    **Calcula el diámetro del cable basado en los parámetros proporcionados.**

    - **Current**: Corriente en amperios (A)
    - **Length**: Longitud del cable en metros (m)
    - **Voltage**: Voltaje en voltios (V)
    - **VoltageDrop**: Caída de tensión en porcentaje (%)
    - **CableType**: Tipo de cable ("copper" o "aluminum")
    """
    try:
        # Aquí puedes agregar la lógica para calcular el diámetro del cable
        if request.cableType == "copper":
            diameter = (request.current * request.length) / (request.voltage * request.voltageDrop)
        else:
            diameter = (request.current * request.length * 1.5) / (request.voltage * request.voltageDrop)
        
        return JSONResponse(content={"diameter": diameter})
    except Exception as e:
        logger.error(f"Error al calcular el diámetro del cable: {e}")
        raise HTTPException(status_code=500, detail=f"Error al calcular el diámetro del cable: {e}")