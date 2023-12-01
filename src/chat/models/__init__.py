from bson import ObjectId
from pydantic import BaseModel, Field
from src.models import PyObjectId
from src.user.models import UserModel
from src.system_profile.models import SystemProfileModel


class MessageModel(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  wa_message_id: str = Field(...)
  content: str = Field(...)
  role: str = Field(...)
  created_at: str = Field(...)

  class Config:
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    schema_extra = {
      "example": {
        "id": "60d5e1d636b7b9f9a9b9b8d7",
        "wa_message_id": "wamid.HBgMNjI4OTc5MjUzOTM1FQIAERgSMUVGRDIyNzVBMzZBODVBNDlFAA==",
        "content": "This is a text message",
        "role": "assistant",
        "created_at": "2023-06-12"
      }
    }, 



class ChatModel(BaseModel):
  id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
  system_profile: SystemProfileModel = Field(...)
  user: UserModel = Field(...)
  messages: list[MessageModel] = Field(default=[])

  class Config:
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    schema_extra = {
      "example": {
        "id": "60d5e1d636b7b9f9a9b9b8d7",
        "system_profile": {
          "whatsapp_id": "123",
          "display_name": "SalmanRF"
        },
        "phone_number": "628978663411",
    }
  }
