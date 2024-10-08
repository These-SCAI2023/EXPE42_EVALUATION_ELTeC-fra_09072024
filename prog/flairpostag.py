from flair.data import Sentence
from flair.models import SequenceTagger







# Load the model
model = SequenceTagger.load("qanastek/pos-french")

sentence = Sentence("Allons, mettons les malheureux dans leur dernière demeure.")

# Predict tags
model.predict(sentence)

# Print predicted pos tags
print(sentence.to_tagged_string())