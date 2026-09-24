"""This code will put 5 lines of text in da frame BIGframe 653947"""
text = [input() for _ in range(5)]
longesttext = max(len(i) for i in text)
print("*"*(longesttext+4))
for i in range(5):
    print(f"* {text[i]}{" "*(longesttext-len(text[i]))} *")
print("*"*(longesttext+4))
