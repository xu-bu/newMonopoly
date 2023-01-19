import random

number=7
l=[0 for _ in range(number)]
loser=[]
for i in range(number):
    dynamites=input("how much dynamites you want to add:")
    if dynamites!=0:
        l += [1 for _ in range(dynamites)]
        random.shuffle(l)
    if l.pop()==1:
        print("boom! congratulations on landing a bomb！")
        loser.append(i)
    else:
        print("well well well, next time you won't be such lucky.")