Values = [1, 9, 10, 12, 14, 1, 2, 3, 17, 5, 7, 10, 10, 1, 18, 3, 9, 11,6,13,12, 20, 4, 17, 15]
Values2=[]
for i in Values:
    if i not in Values2:
        Values2.append(i)
print (Values2)
