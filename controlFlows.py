# if control structure
if 1 == 1:
    if 3 < 2:
        print('3 is less than 2')
    elif 3 == 3:
        print('elif in action kbsa')
    else:
        print("3 is greater than 2")


# for loops
seq = [1, 2, 3, 4, 5, 6]
for item in seq:
    print(item)

d = {"Bill": 1, "Benon": 2, "Clever": 3}
for item in d:
    print(item)

mypairs = [(1, 2), (3, 4), (5, 6)]
for (tup1, tup2) in mypairs:
    print(tup2," tuple 2: ", tup1)

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i + 1
for item in range(10):
    print(item)

# List comprehension
x = [1, 2, 3, 4]
out = [num**2 for num in x]
# for num in x:
#     out.append(num**2)
print(out)
