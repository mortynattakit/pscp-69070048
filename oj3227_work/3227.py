"""This code tell the full name of the card"""
mininame = input().upper()
if len(mininame) == 3:
    num = mininame[0:2]
else:
    num = mininame[0]
group = mininame[-1]
numb = {
    "2":"2","3":"3","4":"4","5":"5",'6':'6',"7":'7','8':'8',
    '9':'9','10':'10',"A":"ace","Q":'queen','J':"jack",'K':"king"
}
groups = {
    'D':'diamonds','S':'spades','H':'hearts','C':'clubs'
}
print(f"{numb[num]} of {groups[group]}")
