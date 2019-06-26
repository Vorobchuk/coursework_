import unittest
from unittest import TestCase
from d_array import DynamicArray
import edamam


class TestRecipe(TestCase):
    def setUp(self):
        self.result = edamam.RecipeSearch({"q": "apple pie", "to": 3}).recipe_results()

    def test_init(self):
        self.assertTrue((type(self.result) == DynamicArray))
        self.assertTrue(self.result[0].label == "Apple Pie Shake")
        self.assertEqual(round(self.result[0].calories, 2), float(539.76))
        self.assertTrue(self.result[0].healthLabels == ["Vegetarian", "Peanut-Free", "Tree-Nut-Free", "Alcohol-Free"])
        self.assertTrue(self.result[0].cautions == ["Sulfites"])
        self.assertTrue(str(self.result[0].ingredients[0]) == "2 scoops vanilla ice cream		WEIGHT:  200.0")
        self.assertTrue(self.result[1].label == "Apple Pie Stuffed French Toast recipes")
        self.assertEqual(round(self.result[1].calories, 2), float(3403.77))
        self.assertTrue(
            self.result[1].healthLabels == ['Sugar-Conscious', 'Vegetarian', 'Tree-Nut-Free', 'Alcohol-Free'])
        self.assertTrue(self.result[1].cautions == ['Milk'])
        self.assertTrue(str(self.result[1].ingredients[1]) == "8 large eggs		WEIGHT:  400.0")
        self.assertTrue(self.result[2].label == "Apple Pie Moonshine")
        self.assertEqual(round(self.result[2].calories, 2), float(1308.46))
        self.assertTrue(
            self.result[2].healthLabels == ['Vegetarian', 'Peanut-Free', 'Tree-Nut-Free', 'Alcohol-Cocktail'])
        self.assertTrue(self.result[2].cautions == ['Wheat', 'Sulfites'])
        self.assertTrue(str(self.result[2].ingredients[0]) == "2 cups  apple juice		WEIGHT:  496.0")


if __name__ == '__main__':
    unittest.main()
