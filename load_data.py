from datasets import load_dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

essay_data = load_dataset('rod101/essay-scoring')

print (essay_data)
print (essay_data['train']['label'][0])

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)
tokenized_essays = essay_data.map(preprocess_function, batched=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

print ("all done")