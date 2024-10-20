import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = TFAutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

data = pd.read_csv('CORE_HackOhio_subset_cleaned_downsampled 1.csv')

key_phrases = data['PNT_ATRISKNOTES_TX']

danger_keywords = [
    'toxic', 'chemicals', 'dangerous', 'danger', 'urgent', 
    'critical', 'burns', 'explosion', 'fire', 'accident', 
    'emergency', 'hazard', 'risk', 'threat', 'radiation', 
    'death', 'crash', 'poor', 'bad', 'lack', 'energy',
    'energized', 'high energy'
]

classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english", tokenizer="distilbert-base-uncased-finetuned-sst-2-english")
results = classifier(key_phrases.tolist())

data['danger_score'] = [1 if result['label'] == 'LABEL_1' else 0 for result in results]

def calculate_importance(phrase):
    score = 0
    for word in danger_keywords:
        if word in phrase.lower():
            score += 1
    return score

data['importance_level'] = key_phrases.apply(calculate_importance)

ranked_data = data.sort_values(by=['danger_score', 'importance_level'], ascending=[False, False])
print(ranked_data.head(20))