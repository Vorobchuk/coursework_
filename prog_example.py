import edamam


def ed_example():
    """Print the example of recipes"""
    dish = 'apple pie'
    to = 3
    result = edamam.RecipeSearch({"q": dish, "to": to}).recipe_results()
    for res in result:
        print("url:  " + res.url)
        print("name: " + res.label)
        print("calories: " + str(round(res.calories, 2)))
        print("labels: " + ", ".join(res.healthLabels))
        if res.cautions:
            print("Cautions: \n".join(res.cautions))
        for i in res.ingredients:
            print(i)
        print("nutrients:")
        string = ""
        for n in res.nutrients:
            string += str(n) + ", "
        print(string)
        print()


ed_example()
