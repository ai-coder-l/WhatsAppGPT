
from pydantic import BaseModel


class WaMessageResMessageSchema(BaseModel):
	id: str = ""


class WaMessageResContactSchema(BaseModel):
	input: str = ""
	wa_id: str = ""


class WaMessageResponseSchema(BaseModel):
	messaging_product: str = "whatsapp"
	contacts: list[WaMessageResContactSchema] = []
	messages: list[WaMessageResMessageSchema] = []

	class Config:
		schema_extra = {
			"messaging_product": "whatsapp",
			"contacts": [
				{
					"input": "16505076520",
					"wa_id": "16505076520"
				}
			],
			"messages": [
				{
					"id": "wamid.HBgLMTY1MDUwNzY1MjAVAgARGBI5QTNDQTVCM0Q0Q0Q2RTY3RTcA"
				}
			]
		}
