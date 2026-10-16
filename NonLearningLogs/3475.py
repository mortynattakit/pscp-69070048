"""This code updates a restaurant menu and prints both orders"""
menu = []
while True:
    text = input()
    if text == "DONE":
        break
    if text == "CLOSED":
        menu.clear()
        break
    if text == "SOMETHING'S WRONG":
        menu.clear()
    elif text.startswith("Can't do: "):
        menu.remove(text[10:])
    else:
        food, course = text.rsplit(" #", 1)
        if course == "N":
            menu.append(food)
        else:
            menu.insert(int(course) - 1, food)
print("Full Course:", menu, "Reversed:", menu[::-1])
