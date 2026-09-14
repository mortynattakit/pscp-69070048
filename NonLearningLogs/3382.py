"""This code will run list but backwards except the NULL input"""
def backward(lst):
    """This function prints the list backwards"""
    if not lst:
        return
    backward(lst[1:])
    print(lst[0])

texts = []
while True:
    text = input()
    if text == "NULL":
        break
    texts.append(text)
backward(texts)
