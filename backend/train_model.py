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

allVarieties = ["Almond milk",
"Almonds",
"Beef",
"Cheese slices",
"Cheese spread",
"Chicken",
"Chocolate",
"Chocolate milk",
"Corn",
"Dried Beef",
"Dry Pasta",
"Fresh ravioli with meat",
"Fresh ravioli with spinach and ricotta",
"Gruyére",
"Ham",
"Lentils",
"Low fat organic milk",
"Non-free range eggs",
"Pancetta",
"Pork",
"Pork sausages",
"Quorn",
"Red kidney beans",
"Rice milk",
"Risotto rice",
"Sliced beef",
"Sliced chicken",
"Smoked cheese",
"Spaghetti Carbonara pre-made meal",
"Tofu",
"UHT milk",
"Vegetarian salami",
"Wholegrain dry pasta",
"Lamb",
"Butter",
"Turkey",
"Rabbit",
"Cod",
"Eggs",
"Insect",
"Whole Milk",
"Wheat",
"Peas",
"Barley",
"Chickpeas"]

inputSet = ["eggs, beaten",
    "milk",
    "beef filet",
    "butter",
    "ground beef",
    "elbow macaroni",
    "egg",
    "Borden® Gouda Cheese Slices, or more as needed",
    "skinless, boneless chicken breast halves",
    "package seasoned coating mix for chicken",
    "chorizo sausage",
    "sausage",
    "chorizo",
    "mascarpone cheese",
    "cheese spread",
    "almond milk",
    "almonds",
    "beef",
    "cheese slices",
    "chicken",
    "chocolate",
    "chocolate milk",
    "corn",
    "dried Beef",
    "dry Pasta",
    "fresh ravioli with meat",
    "fresh ravioli with spinach and ricotta",
    "gruyére",
    "ham",
    "lentils",
    "low fat organic milk",
    "non-free range eggs",
    "pancetta",
    "pork",
    "pork sausages",
    "quorn",
    "red kidney beans",
    "rice milk",
    "risotto rice",
    "sliced beef",
    "sliced chicken",
    "smoked cheese",
    "spaghetti carbonara pre-made meal",
    "tofu",
    "uht milk",
    "vegetarian salami",
    "wholegrain dry pasta",
    "lamb",
    "turkey",
    "rabbit",
    "cod",
    "eggs",
    "insect",
    "whole Milk",
    "wheat",
    "peas",
    "barley",
    "chickpeas",
    "milk, divided",
    "cornstarch",
    "shredded mozzarella cheese",
    "lasagna noodles",
    "grated Parmesan cheese, divided",
    "grated Parmesan cheese",
    "bacon",
    "cream",
    "heavy cream",
    "grated white Cheddar cheese",
    "parmesan cheese",
    "parmesan",
    "wholegrain pasta",
    "wholegrain maccaroni",
    "wholegrain spaghetti",
    "spaghetti",
    "chicken sausage links (such as Aidells®), sliced",
    "chicken sausage links, sliced",
    "chicken sausage, sliced",
    "chicken sausage links",
    "chicken sausage",
    "ricotta cheese gnocchi",
    "cheese gnocchi",
    "gnocchi",
    "egg noodles",
    "noodles",
    "frozen green soybeans, thawed",
    "green soybeans, thawed",
    "frozen green soybeans",
    "green soybeans",
    "green soybeans",
    "green beans",
    "soybeans",
    "pasta",
    "country style pork ribs",
    "pork ribs",
    "ribs",
    "spare ribs"]
varietyList_O =["Eggs",
    "Whole Milk",
    "Beef",
    "Butter",
    "Beef",
    "Dry Pasta",
    "Eggs",
    "Cheese slices",
    "Chicken",
    "Chicken",
    "Pork sausages",
    "Pork sausages",
    "Pork sausages",
    "Cheese spread",
    "Cheese spread",
    "Almond milk",
    "Almonds",
    "Beef",
    "Cheese slices",
    "Chicken",
    "Chocolate",
    "Chocolate milk",
    "Corn",
    "Dried Beef",
    "Dry Pasta",
    "Fresh ravioli with meat",
    "Fresh ravioli with spinach and ricotta",
    "Gruyére",
    "Ham",
    "Lentils",
    "Low fat organic milk",
    "Non-free range eggs",
    "Pancetta",
    "Pork",
    "Pork sausages",
    "Quorn",
    "Red kidney beans",
    "Rice milk",
    "Risotto rice",
    "Sliced beef",
    "Sliced chicken",
    "Smoked cheese",
    "Spaghetti Carbonara pre-made meal",
    "Tofu",
    "UHT milk",
    "Vegetarian salami",
    "Wholegrain dry pasta",
    "Lamb",
    "Turkey",
    "Rabbit",
    "Cod",
    "Eggs",
    "Insect",
    "Whole Milk",
    "Wheat",
    "Peas",
    "Barley",
    "Chickpeas",
    "Whole Milk",
    "Corn",
    "Cheese slices",
    "Dry Pasta",
    "Cheese slices",
    "Cheese slices",
    "Pork",
    "Whole Milk",
    "Whole Milk",
    "Cheese slices",
    "Cheese slices",
    "Cheese slices",
    "Wholegrain dry pasta",
    "Wholegrain dry pasta",
    "Wholegrain dry pasta",
    "Dry Pasta",
    "Chicken",
    "Chicken",
    "Chicken",
    "Chicken",
    "Chicken",
    "Dry Pasta",
    "Dry Pasta",
    "Dry Pasta",
    "Dry Pasta",
    "Dry Pasta",
    "Red kidney beans",
    "Red kidney beans",
    "Red kidney beans",
    "Red kidney beans",
    "Red kidney beans",
    "Red kidney beans",
    "Red kidney beans",
    "Dry Pasta",
    "Pork",
    "Pork",
    "Pork",
    "Pork"]
for i in range(len(varietyList_O)):
    varietyList_O[i] = allVarieties.index(varietyList_O[i])

varietyList = to_categorical(varietyList_O)
max_length_ingredient = 8;
most_used_words = 2000
top_x = filter_to_top_x(inputSet,most_used_words,0)[1]
print(type(top_x))
inputSet, word_list = filter_to_top_x(inputSet,most_used_words,0)
print(inputSet)
print("----")
testSet, word_list = convertToModelInput(["bacon"],top_x)
print(testSet)
inputSet = sequence.pad_sequences(inputSet, maxlen=max_length_ingredient)

train_x, test_x, train_y, test_y = train_test_split(inputSet, varietyList, test_size=0.0)

embedding_vector_length = 64
model = Sequential()

model.add(Embedding(most_used_words, embedding_vector_length, input_length=max_length_ingredient))
model.add(Conv1D(50, 5)) # 50 5
model.add(Flatten())
model.add(Dense(100, activation='relu')) #100
model.add(Dense(max(varietyList_O) + 1, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_x, train_y, epochs=100, batch_size=64)

y_score = model.predict(test_x)
y_score = [[1 if i == max(sc) else 0 for i in sc] for sc in y_score]
n_right = 0
# for i in range(len(y_score)):
#     if all(y_score[i][j] == test_y[i][j] for j in range(len(y_score[i]))):
#         n_right += 1

#print("Accuracy: %.2f%%" % ((n_right/float(len(test_y)) * 100)))
result = model.predict(sequence.pad_sequences(testSet, maxlen=max_length_ingredient))
result = result.tolist()
print(result)
print(max(result[0]))
print(result[0].index(max(result[0])))
print(allVarieties[result[0].index(max(result[0]))])
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
        pickle.dump(allVarieties, f, pickle.HIGHEST_PROTOCOL)
