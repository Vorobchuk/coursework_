import requests
from d_array import DynamicArray
from api_data import get_id, get_key


class RecipeSearch:
    """Search a recipe"""

    def __init__(self, parameters={}):
        """
        Initialize the parameters for request response
        :param parameters: (API ID, API Key)
        """
        self.parameters = parameters
        self.parameters["app_id"] = get_id()
        self.parameters["app_key"] = get_key()
        self._request = None
        self.urlbase = "https://api.edamam.com/search"

    def recipe_results(self):
        """
        Get the recipe according to the request
        :return: list of all recipes
        """
        self._request = requests.get(self.urlbase, params=self.parameters)
        hits = self._request.json()["hits"]
        result = DynamicArray()
        print(hits)
        for hit in hits:
            result.append(Recipe(hit["recipe"]))
        return result


class Recipe:

    def __init__(self, source=None):
        """
        Initialize the parameters of the recipe
        :param source: one of the keys in JSON file
        """
        if source is not None:
            self.uri = source["uri"]
            self.label = source["label"]
            self.image = source["image"]
            self.source = source["source"]
            self.url = source["url"]
            self.dietLabels = source["dietLabels"]
            self.healthLabels = source["healthLabels"]
            self.cautions = source["cautions"]
            self.calories = source["calories"]
            self.totalWeight = source["totalWeight"]
            self.ingredients = [Ingredient(x) for x in source["ingredients"]]
            self.nutrients = [Nutrient(source["totalNutrients"][x]) for x in source["totalNutrients"]]
            self.totalDaily = source["totalDaily"]
        else:
            self.uri = None
            self.label = None
            self.image = None
            self.source = None
            self.url = None
            self.dietLabels = None
            self.healthLabels = None
            self.cautions = None
            self.makes = None
            self.calories = None
            self.totalWeight = None
            self.ingredients = None
            self.totalNutrients = None
            self.totalDaily = None


class Ingredient:

    def __init__(self, source=None):
        """
        Initialize the ingredients of the recipe
        :param source: one of the keys in JSON file
        """
        self.source = source
        if source is not None:
            self.text = source["text"]
            self.weight = source["weight"]
        else:
            self.text = None
            self.weight = None

    def __str__(self):
        """
        Represent the ingredient of the recipe
        :return: string
        """
        string = ""
        string += self.source['text'] + "\t\t" + "WEIGHT:  " + str(round(self.source['weight'], 2))
        return string


class Nutrient:

    def __init__(self, source=None):
        """
        Initialize the nutrients if the ingredients
        :param source: one of the keys in JSON file
        """
        self.source = source
        if source is not None:
            self.label = source["label"]
            self.quantity = source["quantity"]
            self.unit = source["unit"]
        else:
            self.label = None
            self.quantity = None
            self.unit = None

    def __str__(self):
        """
        Represent the nutrient of the ingredient
        :return: string
        """
        string = ""
        string += self.source['label'] + ":" + str(round(self.source['quantity'], 2))
        return string


if __name__ == "__main__":
    to = 5
    dish = "apple cake"
    test = RecipeSearch({"q": dish, "to": to}).recipe_results()
    print(test)
