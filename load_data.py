from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

# Load the dataset
essay_data = load_dataset('rod101/essay-scoring')

# Print dataset information and a sample label
print(essay_data)
print(essay_data['train']['label'][0])

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

# Define the preprocessing function
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

# Tokenize the essays
tokenized_essays = essay_data.map(preprocess_function, batched=True)

# Define the label adjustment function
def adjust_labels(examples):
    examples['label'] = [label for label in examples['label']]
    return examples

# Adjust the labels to the range 0-8
tokenized_essays = tokenized_essays.map(adjust_labels, batched=True)
# Initialize the data collator
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

print("All done")