class TrainingSet:

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
        "Chickpeas",
        "Apple",
        "Honey",
        "Rice",
        "Cauliflower",
        "Carrot",
        "Broccoli",
        "Bell Pepper",
        "Black and white Pepper",
        "Olive Oil",
        "Olive",
        "Onions",
        "Potatoes",
        "Sunflower Oil",
        "Raw Sugar",
        "Salt",
        "Soybean",
        "Spinach",
        "Tomatoe",
        "Sweet Potatoe"]

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
        "spare ribs",
        "fish",
        "fishs",
        "salmon",
        "salmons",
        "fish sticks",
        "fish stick",
        "seabreams",
        "seabream",
        "apple",
        "apples",
        "honey",
        "comb honey",
        "liquid honey",
        "granulated honey",
        "creamed honey",
        "chunk honey",
        "rice",
        "brown rice",
        "basmati",
        "basmati rice",
        "arborio",
        "arborio rice",
        "white rice",
        "jasmine rice",
        "jasmine",
        "cauliflower",
        "cauliflowers",
        "cauliflower rice",
        "carrot",
        "carrots",
        "carrot sliced",
        "carrots sliced",
        "carrot slice",
        "broccolis",
        "broccoli"
        "broccoli scrambled",
        "bell pepper",
        "bell peppers",
        "yellow bell pepper",
        "yellow bell peppers",
        "red bell pepper",
        "red bell peppers",
        "green bell pepper",
        "green bell peppers",
        "chilli",
        "chillies",
        "pepperoni",
        "pepperoni",
        "pepper",
        "black pepper",
        "white pepper",
        "olive oil",
        "oliv oil",
        "olive",
        "olives",
        "olive sliced",
        "olives sliced",
        "onions",
        "onion",
        "onions sliced",
        "onion rings",
        "potatoes",
        "potatoe",
        "potatoe wedges",
        "fries",
        "french fries",
        "pommes",
        "pommes frites",
        "sunflower oil",
        "oil",
        "raw sugar",
        "sugar",
        "white sugar",
        "brown sugar",
        "salt",
        "soybeans",
        "soybean",
        "soy beans",
        "soy bean",
        "spinach",
        "creamed spinach",
        "cream spinach",
        "young spinach",
        "leaf spinach",
        "tomatoes",
        "tomatoe",
        "tomatoe sauce",
        "tomatoe paste",
        "sweet potatoe",
        "sweet potatoes",
        "sweet potatoe wedges",
        "sweet potatoe fries",
        "steak",
        "steaks"]
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
        "Pork",
        "Cod",
        "Cod",
        "Cod",
        "Cod",
        "Cod",
        "Cod",
        "Cod",
        "Cod",
        "Apple",
        "Apple",
        "Honey",
        "Honey",
        "Honey",
        "Honey",
        "Honey",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Rice",
        "Cauliflower",
        "Cauliflower",
        "Cauliflower",
        "Carrot",
        "Carrot",
        "Carrot",
        "Carrot",
        "Carrot",
        "Broccoli",
        "Broccoli",
        "Broccoli",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Bell Pepper",
        "Black and white Pepper",
        "Black and white Pepper",
        "Black and white Pepper",
        "Olive Oil",
        "Olive Oil",
        "Olive",
        "Olive",
        "Olive",
        "Olive",
        "Onions",
        "Onions",
        "Onions",
        "Onions",
        "Potatoes",
        "Potatoes",
        "Potatoes",
        "Potatoes",
        "Potatoes",
        "Potatoes",
        "Potatoes",
        "Sunflower Oil",
        "Sunflower Oil",
        "Raw Sugar",
        "Raw Sugar",
        "Raw Sugar",
        "Raw Sugar",
        "Salt",
        "Soybean",
        "Soybean",
        "Soybean",
        "Soybean",
        "Spinach",
        "Spinach",
        "Spinach",
        "Spinach",
        "Spinach",
        "Tomatoe",
        "Tomatoe",
        "Tomatoe",
        "Tomatoe",
        "Sweet Potatoe",
        "Sweet Potatoe",
        "Sweet Potatoe",
        "Sweet Potatoe",
        "Pork",
        "Pork"]