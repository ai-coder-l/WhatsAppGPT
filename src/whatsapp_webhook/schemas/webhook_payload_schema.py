from datetime import datetime
from pydantic import BaseModel, Field


class WaMessageText(BaseModel):
	body: str = Field(...)


class WaMessage(BaseModel):
	id: str = Field(...)
	message_type: str = Field(alias="type")
	text: WaMessageText = Field(...)
	timestamp: str = Field(...)


class WaContactProfile(BaseModel):
	name: str = Field(...)


class WaContact(BaseModel):
	wa_id: str = Field(...)
	profile: WaContactProfile = Field(...)


class WaPayloadMetadata(BaseModel):
	display_phone_number: str = Field(...)
	phone_number_id: str = Field(...)


class WaPayloadChangesValue(BaseModel):
	messaging_product: str = Field(...)
	metadata: WaPayloadMetadata = Field(...)
	messages: list[WaMessage] = Field(default=[])
	contacts: list[WaContact] = Field(default=[])


class WaPayloadEntryChanges(BaseModel):
	value: WaPayloadChangesValue = Field(...)
	field: str = Field(...)


class WaPayloadEntry(BaseModel):
	id: str = Field(...)
	changes: list[WaPayloadEntryChanges] = Field(default=[])


class WaWebhookPayload(BaseModel):
	object_name: str = Field(alias="object")
	entry: list[WaPayloadEntry] = []

	class Config:
		schema_extra = {
			"object": "whatsapp_business_account",
			"entry": [{
				"id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
				"changes": [{
					"value": {
						"messaging_product": "whatsapp",
						"metadata": {
							"display_phone_number": "PHONE_NUMBER",
							"phone_number_id": "PHONE_NUMBER_ID"
						},
						# specific Webhooks payload
					},
					"field": "messages"
				}]
			}]
		}
