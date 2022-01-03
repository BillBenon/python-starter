# Lists
# mylist = ['a', 'b', 'c', 'd']
# mylist = ['billbenon', 1, 2, 3, 23.2, True, 'dushime', [1, 2, 3]]

# print(mylist[:3])
# print(mylist[1:3])
# print('before reassignment:')
# mylist[0] = 'NEW ITEM'
# print('after reassignment')
# print(mylist)

# mylist.append('NEW ITEM')
# listTwo = ['x', 'y', 'z']
# mylist.append(listTwo)
# mylist.extend(listTwo)
# print(mylist)

# item = mylist.pop()
# print(mylist)
# print(item)
# mylist.reverse()
# print(mylist)

# print(len(mylist))

# mylist = [4, 6, 1, 7, 43, 2]
# mylist.sort()
# print(mylist)

# mylist = [1, 2, ['x', 'y', 'z']]
# print(mylist[2][1])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)
