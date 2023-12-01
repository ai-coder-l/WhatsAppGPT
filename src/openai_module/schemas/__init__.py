from pydantic import BaseModel

from src.config import config


class ChatCompletionOptionsSchema(BaseModel):
  model: str = "gpt-3.5-turbo"
  temperature: int = 1
  max_tokens: int = config.OPENAI_CHAT_MAX_TOKEN


class ChatCompletionMessageSchema(BaseModel):
  role: str
  content: str
  name: str = ""


class ChatCompletionResMessageSchema(BaseModel):
  role: str
  content: str


class ChatCompletionChoiceSchema(BaseModel):
  index: int
  message: ChatCompletionResMessageSchema
  finish_reason: str


class ChatCompletionUsageSchema(BaseModel):
  prompt_tokens: int
  completion_tokens: int
  total_tokens: int


class ChatCompletionResponseSchema(BaseModel):
  id: str
  object: str
  created: int
  choices: list[ChatCompletionChoiceSchema]
  usage: ChatCompletionUsageSchema

  class Config:
    schema_extra = {
      "id": "chatcmpl-123",
      "object": "chat.completion",
      "created": 1677652288,
      "choices": [{
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "\n\nHello there, how may I assist you today?",
        },
        "finish_reason": "stop"
      }],
      "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
      }
    }
