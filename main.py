from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import joblib

class Model1:
    def __init__(self, age, gender):

        self.age = age
        self.gender = gender

    def result(self):
    
        model = joblib.load('bot.joblib')
        results = model.predict([[self.age, self.gender]])
        print("Your prediction is : " + str(results))


def show_menu():
    print("\nMusic Recomendation")
    print("We will need your age and gender !")


def get_gender():
    while True:
        try:
            gender = int(input("What is your gender (0 for woman, 1 for man): "))
            if gender not in [0, 1]:
                print("Invalid input. Gender must be 0 or 1.")
            else:
                return gender
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def main():
    while True:
        age = int(input("What is your age:\n"))
        gender = get_gender()
        md = Model1(age, gender)
        md.result()

if __name__ == "__main__":
    main()
