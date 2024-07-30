# Essay-scoring-LLM
An LLM for scoring your essays for free.


### Essay 1 (a bad student writing about environment) - AI-rating: 4/10

The environment is like super important, you know? Like, we need to keep it clean and stuff because if not, things get bad. There’s garbage everywhere and that’s no good. I think people should throw their trash in the bins, or maybe even better, just recycle. Trees are cool too, so we should have more of them because they help make air or something. Pollution is bad, so we need to stop that. It’s like when you have too much junk food, but for the Earth. So let’s all just be better and not mess up the planet. Thanks.

### Essay 2 (a good student writing about environment) - AI-rating: 7/10

The environment is a crucial aspect of our planet that requires immediate and sustained attention. As we continue to advance technologically and economically, the strain we place on natural resources becomes increasingly evident. The degradation of ecosystems, loss of biodiversity, and the impacts of climate change are all pressing concerns that must be addressed to ensure a sustainable future.

One of the primary challenges we face is pollution, which affects air, water, and soil quality. Air pollution from industrial emissions and vehicle exhaust contributes to health problems and global warming. Similarly, water pollution from chemical runoff and plastic waste disrupts aquatic life and contaminates drinking water sources. Addressing these issues requires comprehensive strategies, including stricter regulations, increased use of renewable energy, and improved waste management practices.

Preserving natural habitats and promoting biodiversity are also essential. Deforestation and habitat destruction threaten countless species and disrupt ecological balance. Conservation efforts, such as establishing protected areas and promoting sustainable land use practices, are critical to safeguarding these ecosystems.

Ultimately, individual actions combined with collective policy changes can make a significant difference. By adopting eco-friendly habits, supporting environmental policies, and advocating for change, we can contribute to the preservation of our planet for future generations. Our collective efforts are essential in fostering a healthier, more sustainable environment.


## Fine-tune the model yourself! Follow these steps:
* Clone the repo
```python
git clone __
cd Essay-scoring-LLM
```
* Create virtual environment and install dependencies
```python
#Create your virtual environment (alternatively, use conda)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
* Load the data from the data from the essays + ratings dataset: https://huggingface.co/datasets/rod101/essay-scoring.
This will load the data and initialize the tokenizer (text encoder) used by "distilbert/distilbert-base-uncased" open-source model.
```python
python3 load_data.py
```
* Initialize and train the model.
You can change parameters under the "Training" class. The default configurations can be found on the original script.
Running training.py will also create a new folder named "my_awesome_model" and save it there all the model's weight at different timesteps.
```python
python3 training.py
```

* Run inference
Change the texts file for your final text. Add your text to the script by passing it to the 'texts' array. 
```python
python3 inference.py
```

### Enjoy!




