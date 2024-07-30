from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("my_awesome_model/checkpoint-350")
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

# Prepare your text for inference
texts = [
        '''
Your text here.

        '''
]
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Get predictions
logits = outputs.logits
print (f"logits: {logits}")
predicted_labels = logits.argmax(axis=-1).tolist()

# Convert numeric labels to their string equivalents if needed
id2label = {i: str(i) for i in range(11)}
predicted_labels_str = [id2label[label] for label in predicted_labels]

print(predicted_labels_str)
print (f"final essay score: {int(predicted_labels_str[0]) +2}")