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
from trainingsdata import TrainingSet
varietyListO = TrainingSet.varietyList_O
for i in range(len(varietyListO)):
    varietyListO[i] = TrainingSet.allVarieties.index(TrainingSet.varietyList_O[i])

varietyList = to_categorical(varietyListO)
max_length_ingredient = 8;
most_used_words = 2000
top_x = filter_to_top_x(TrainingSet.inputSet,most_used_words,0)[1]
inputSetFiltered, word_list = filter_to_top_x(TrainingSet.inputSet,most_used_words,0)
inputSetFiltered = sequence.pad_sequences(inputSetFiltered, maxlen=max_length_ingredient)

train_x, test_x, train_y, test_y = train_test_split(inputSetFiltered, varietyList, test_size=0.0)

embedding_vector_length = 64
model = Sequential()

model.add(Embedding(most_used_words, embedding_vector_length, input_length=max_length_ingredient))
model.add(Conv1D(50, 5)) # 50 5
model.add(Flatten())
model.add(Dense(100, activation='relu')) #100
model.add(Dense(max(varietyListO) + 1, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_x, train_y, epochs=100, batch_size=64)

y_score = model.predict(test_x)
y_score = [[1 if i == max(sc) else 0 for i in sc] for sc in y_score]
n_right = 0
# for i in range(len(y_score)):
#     if all(y_score[i][j] == test_y[i][j] for j in range(len(y_score[i]))):
#         n_right += 1

#print("Accuracy: %.2f%%" % ((n_right/float(len(test_y)) * 100)))
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
with open('topx.pkl', 'wb+') as f:
        pickle.dump(top_x, f, pickle.HIGHEST_PROTOCOL)
with open('allvarieties.pkl', 'wb+') as f:
        pickle.dump(TrainingSet.allVarieties, f, pickle.HIGHEST_PROTOCOL)
