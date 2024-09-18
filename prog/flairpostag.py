from flair.data import Sentence
from flair.models import SequenceTagger

# Load the model
model = SequenceTagger.load("qanastek/pos-french")

sentence = Sentence("George Washington est allé à Washington")

# Predict tags
model.predict(sentence)

# Print predicted pos tags
print(sentence.to_tagged_string())