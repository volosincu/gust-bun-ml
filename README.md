# gust-bun-ml
Un model tf de generat rețete culinare

Jupyter [notebook](https://colab.research.google.com/drive/1TeiDVxUlqhB_xcZaRmo_uzvrjF_Wmelx?usp=sharing)

Resurse tensorflow pe aceiași temă:
 - [Text generation with an RNN](https://www.tensorflow.org/text/tutorials/text_generation)
 - [Sequential models](https://www.tensorflow.org/guide/keras/sequential_model)
 - [How to save a model](https://www.tensorflow.org/guide/saved_model)
 - [Federated Learning for Text Generation](https://www.tensorflow.org/federated/tutorials/federated_learning_for_text_generation)

Dimensionality-reduction algorithms
 - [Embeddings explained](https://towardsdatascience.com/how-to-create-word-embedding-in-tensorflow-ed0a61507dd0)
 - [tSNE explained](https://distill.pub/2016/misread-tsne/)
 - [PCA example](https://setosa.io/ev/principal-component-analysis/)

Sursa rețete: [www.e-retete.ro](https://www.e-retete.ro/)

-----------
Team:
 - Cosmin Lupu
 - Oica Andra
 - Ervin Maftei
 - Volosincu Bogdan

-----------
To do:
- Add recipes to training data file (Ervin)
- Add recipes to test data file (Ervin)
- N-gram model (tokens, bigrams...) (Bogdan+Andra)
```
Methods:
1.
-- Create bigram probability table
-- Create a routine for validating recipe generation
2. (possible future idea)
-- Training > Analyzing weights based on the bigram model
```
- Generate data evaluation matrix (Cosmin)
- Normalize better tokenization (START-END of recipes, /n...) (Bogdan)
- Word-based vs Character-based (documentation, at least)
- UI (Andra)

-----------
## Steps to make your project work

Set up virtual environment (Once)
-- in the project folder
```
python -m venv ./env
```
Activate it (Each time, before running project)
-- preferably ran through git bash
```
source env/Scripts/activate
```
To deactivate it
```
deactivate
```
Install python libraries with pip (When needed, before running project)
```
pip install -r req.txt
```
Run django project at *http://127.0.0.1:8000/* (Each time)
```
python manage.py runserver
```
