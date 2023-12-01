from pydantic import BaseSettings

class Config(BaseSettings):
  MONGODB_URI: str = "YOUR MONGODB URI"
  MONGO_INITDB_DATABASE: str = "YOUR MONGO DB NAME"
  WHATSAPP_WEBHOOK_VERIFY_TOKEN: str = "YOUR WHATSAPP WEBHOOK VERIFY TOKEN"
  OPENAI_API_KEY: str = "YOUR OPENAI API KEY"
  OPENAI_CHAT_MAX_TOKEN: int = 1000  # Example value
  FACEBOOK_API_URL: str = "YOUR FACEBOOK API URL"
  FACEBOOK_APP_SECRET: str = "YOUR FACEBOOK APP SECRET"
  WHATSAPP_ACCESS_TOKEN: str = "YOUR WHATSAPP ACCESS TOKEN"
  ADMIN_JWT_SECRET: str = "YOUR ADMIN JWT SECRET"
  JWT_ALGORITHM: str = "YOUR JWT ALGORITHM"
  ENV: str = "development"  # or 'production'
  PORT: int = 8000  # Example port number
  WEAVIATE_URL: str = "YOUR WEAVIATE URL"
  WEAVIATE_API_KEY: str = "YOUR WEAVIATE API KEY"
  
  class Config:
    env_file = "./src/.env"

config = Config()

