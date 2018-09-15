from nltk import word_tokenize
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from filter_and_replace_words import filter_to_top_x
from filter_and_replace_words import convertToModelInput
import numpy
import pickle
from keras.models import model_from_json

def predict(inputSet):
    max_length_ingredient = 8;
    top_x = {}
    with open('topx.pkl', 'rb') as f:
        top_x = pickle.load(f)
    with open('allvarieties.pkl', 'rb') as f:
        allVarieties = pickle.load(f)

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    #print("Loaded model from disk")
    ingredients = []
    for ingredient in inputSet:
        testSet, word_list = convertToModelInput([ingredient],top_x)
        result = loaded_model.predict(sequence.pad_sequences(testSet, maxlen=max_length_ingredient))
        result = result.tolist()
        if max(result[0]) < 0.01:
            result = "undefined"
        else:
            result = allVarieties[result[0].index(max(result[0]))]
        ingredients.append(result)
    return ingredients
