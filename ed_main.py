from edamam import RecipeSearch, Recipe, Ingredient, Nutrient
from d_array import DynamicArray


intro = "Hello! This is a program to find any recipe you want.\n You can also enter some characteristics to your dish."\
    "\nHere you can not only find a recipe, but also find out how much calories does your dish have,\n from what "\
    "nutrients does it consists and to what categories it belongs.\nLet's start!"
print(intro)
try:
    dish = str(input("Enter a dish to find a recipe: "))
except ValueError:
    print("NO RECIPES. Please enter a dish correctly")
    dish = str(input("Enter a dish: "))
try:
    to = int(input("Enter number of recipes: "))
except ValueError:
    to = 5
test = RecipeSearch({"q": dish, "to": to}).recipe_results()


def to_print(i):
    """Print main information"""
    print("Click here to learn more:  " + i.url)
    print("Name: " + i.label)
    print("Calories: " + str(round(i.calories, 2)))
    print("Labels: " + ", ".join(i.healthLabels))
    if i.cautions:
        print("CAUTIONS!!!\n", "Contains: " + ", ".join(i.cautions))
    for ingr in i.ingredients:
        print(ingr)
    print("All nutrients:")
    string = ""
    for n in i.nutrients:
        string += str(n) + ", "
    print(string)
    print()


def main():
    """This is the main function"""
    hl = "health labels: [Alcohol-Free, Fish-Free, Low-Sugar, Peanut-Free, Soy-Free, Vegan, Vegetarian]"
    d = "diets: [High-Fiber, High-Protein, Low-Carb, Low-Fat, Balanced]"
    try:
        cal = int(input("Enter number of max calories or enter '0' if it doesn't matter: "))
    except ValueError:
        cal = 0
    label_and_diet = DynamicArray()
    print("do you want to choose label?" + "\n" + hl)
    label = input("yes/no: ")
    if label == "yes":
        labels = input("Enter labels: ")
        labels = labels.split()
        for l in labels:
            label_and_diet.append(l)
    print("do you want to choose diet?" + "\n" + d)
    diet = input("yes/no: ")
    if diet == "yes":
        diets = input("Enter diet: ")
        diets = diets.split()
        for d in diets:
            label_and_diet.append(d)
    your_charac = []
    result = False
    for j in test:
        if cal >= j.calories or cal == 0:
            if not label_and_diet:
                to_print(j)
                result = True
            else:
                for characteristic in label_and_diet:
                    if characteristic in j.healthLabels or characteristic in j.dietLabels:
                        your_charac.append(j)

    if your_charac or result:
        for charac in your_charac:
            to_print(charac)
    else:
        print("No recipes for these labels or diet")
        print("PLEASE CHOOSE ANOTHER LABEL OR DIET OR ENTER MORE CALORIES")


main()
