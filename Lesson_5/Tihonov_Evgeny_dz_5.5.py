src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
uniqueList = []
for item in src:
    itemExist = False
    for x in uniqueList:
        if x == item:
            itemExist = True
            break
    if not itemExist:
        uniqueList.append(item)
print(uniqueList)

print('='*40)

uniqueList2 = [i for i in src if src.count(i) == 1]
print(uniqueList2)
