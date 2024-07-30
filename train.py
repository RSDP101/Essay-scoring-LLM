import os
from load_data import tokenized_essays, tokenizer, data_collator
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

# Environment variable for CUDA debugging
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

# Mapping from label index to label value and vice versa
id2label = {i: str(i) for i in range(11)}  # Maps 0-8 to 2-10
label2id = {str(i): i for i in range(11)}  # Maps 2-10 to 0-8

# Load the model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert/distilbert-base-uncased", num_labels=11, id2label=id2label, label2id=label2id
)

# Define training arguments
training_args = TrainingArguments(
    output_dir="my_awesome_model",
    learning_rate=2e-5,
    per_device_train_batch_size=8,  # Reduced batch size
    per_device_eval_batch_size=8,   # Reduced batch size
    num_train_epochs=5,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_essays["train"],
    eval_dataset=tokenized_essays["train"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Start training
trainer.train()