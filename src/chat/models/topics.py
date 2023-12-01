
TopicModel = {
  "class": "Topics",
  "properties": [
    {
      "name": "topic",
      "dataType": ["text"],
      "moduleConfig": {
        "text2vec-openai": {
          "vectorizePropertyName": False
        }
      }
    },
    ],
  "vectorizer": "text2vec-openai",
  "moduleConfig": {
    "text2vec-openai": {
      "vectorizeClassName": False
    }
  }
}