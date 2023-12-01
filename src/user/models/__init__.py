from pydantic import BaseModel, Field
from bson import ObjectId
from src.models import PyObjectId

class UserBioModel(BaseModel):
  full_name: str = Field(default=None)
  date_of_birth: str = Field(default=None, description="Date of birth in YYYY-MM-DD format")
  gender: str = Field(default=None, description="User's gender: (Male|Female)")
  interests: list[str] = Field(default=[], description="List of user's interest, can be deducted from chat topics")
  relationship_goal: str = Field(default=None, description="Could be one of: casual, short-term, long-term")
  

class UserModel(BaseModel):
  _id: PyObjectId = Field(default_factory=PyObjectId)
  phone_number: str = Field(default="")
  whatsapp_id: str = Field(default="")
  name: str = Field(default="")
  bio_information: UserBioModel = Field(default=None)

  class Config:
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
    schema_extra = {
      "example": {
        "_id": "60d5e1d636b7b9f9a9b9b8d7",
        "full_name": "Salman Rizqi Fatih",
        "phone_number": "628976664322",
      }
    }

  def fromDict(userDict: dict):
    return UserModel.parse_obj(userDict)
