"""This code checks the ingredients and taste of Pad Thai"""
recipe = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
          "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg",
          "Oil", "Peanuts"}
ingredients = set()
while True:
    text = input()
    if text == "Cook":
        break
    ingredients.add(text)
tastes = set()
while True:
    text = input()
    if text == "End":
        break
    tastes.add(text)
if ingredients - recipe:
    print("This is not Pad Thai!!!")
elif ingredients != recipe:
    print("This is bad!")
elif tastes != {"Sweet", "Sour", "Salty"}:
    print("Not Bad...")
else:
    print("Delicious!")
