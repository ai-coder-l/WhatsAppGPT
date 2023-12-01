def flatten_dict(criteria: dict, prefix: str = ""):
  result = {}
  
  for key, value in criteria.items():
    path = key 

    if prefix != "":
      path = f"{prefix }.{key}"
    
    if isinstance(value, dict):
      result = {**result, **flatten_dict(value, path)}
      continue
    
    result[path] = value

  return result