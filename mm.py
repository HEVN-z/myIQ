ballance = 100
money = ballance
pocket1 = (money/3).__floor__()
pocket2 = (money/3).__floor__()
pocket3 = (money/3).__floor__()
print("pocket 1 =",pocket1,"pocket 2 =",pocket2,"pocket 3 =",pocket3)
while(True):
    if pocket1 == pocket2 == pocket3:
        print("All pocket are equal")
        break
    else:
        print("All pocket are not equal")
        break