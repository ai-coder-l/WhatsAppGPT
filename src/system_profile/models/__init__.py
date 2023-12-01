from bson import ObjectId
from pydantic import BaseModel, Field
from src.models import PyObjectId


class SystemProfileModel(BaseModel):
  _id: PyObjectId = Field(default_factory=PyObjectId)
  whatsapp_id: str = Field(...)
  display_name: str = Field(default="")

  class Config:
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    schema_extra = {
      "example": {
        "whatsapp_id": "123",
        "display_name": "SalmanRF"
      }
    }
