import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import tree


music_data = pd.read_csv("music.csv")

# # 2 data sets
no_genre = music_data.drop(columns='genre')
with_genre = music_data['genre']

model = DecisionTreeClassifier()
model.fit(no_genre, with_genre)
#Graphical visualization 
tree.export_graphviz(model , out_file='graphical.dot' , feature_names= ['age' , 'gender'] , class_names= sorted(with_genre.unique()) , label= 'all'  , rounded= True , filled= True)

#Creating a trainend model into a file for easier use
trained_model = joblib.dump(model, 'bot.joblib')

print("Success : " + str(trained_model))
