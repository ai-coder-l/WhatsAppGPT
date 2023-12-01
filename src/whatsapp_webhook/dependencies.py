import hashlib
import json
from src.config import config


def validate_whatsapp_webhook_payload(data: dict) -> str:
  json_str = json.dumps(data, sort_keys=True)

  data_with_secret = json_str + config.FACEBOOK_APP_SECRET

  sha256_hash = hashlib.sha256()

  data_bytes = data_with_secret.encode('utf-8')

  sha256_hash.update(data_bytes)

  hex_digest = sha256_hash.hexdigest()

  return hex_digest
