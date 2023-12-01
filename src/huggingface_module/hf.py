from transformers import pipeline, Pipeline

class HuggingFace():
  classifier: Pipeline = None

  def init(self):
    self.classifier = pipeline(
      task="zero-shot-classification",
      model="facebook/bart-large-mnli"
    )

  def get_classifier(self) -> Pipeline:
    return self.classifier


hf = HuggingFace()