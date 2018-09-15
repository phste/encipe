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
class Predictor:
    top_x = 0
    max_length_ingredient =0 

    allVarieties = 0
    loaded_model = 0
    def __init__(self):
        self.max_length_ingredient = 8;
        self.top_x = {}
        with open('topx.pkl', 'rb') as f:
            self.top_x = pickle.load(f)
        with open('allvarieties.pkl', 'rb') as f:
            self.allVarieties = pickle.load(f)

        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("model.h5")
    def predict(self, inputSet):

        ingredients = []
        for ingredient in inputSet:
            testSet, word_list = convertToModelInput([ingredient],self.top_x)
            result = self.loaded_model.predict(sequence.pad_sequences(testSet, maxlen=self.max_length_ingredient))
            result = result.tolist()
            if max(result[0]) < 0.01:
                result = "undefined"
            else:
                result = self.allVarieties[result[0].index(max(result[0]))]
            ingredients.append(result)
        return ingredients
