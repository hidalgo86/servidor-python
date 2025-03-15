from pydantic import BaseModel, Field

class CableCalculationRequest(BaseModel):
    current: float = Field(..., description="Corriente en amperios (A)")
    length: float = Field(..., description="Longitud del cable en metros (m)")
    voltage: float = Field(..., description="Voltaje en voltios (V)")
    voltageDrop: float = Field(..., description="Caída de tensión en porcentaje (%)")
    cableType: str = Field(..., description='Tipo de cable ("copper" o "aluminum")')

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                "current": 10.0,
                "length": 50.0,
                "voltage": 220.0,
                "voltageDrop": 2.0,
                "cableType": "copper"
                }
            ]
        }
    }