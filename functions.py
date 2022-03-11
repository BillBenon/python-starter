def my_func(param1="default"):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))


my_func()


def hello():
    return "hello"


result = hello()
print(result)


def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers"


result = addNum(2, 3)
print(type(result))

# Lambda Expression

# Filter
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

# def even_bool(num):
#     return num % 2 == 0
#
# evens = filter(even_bool, mylist)
# print(list(evens))

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))

tweet = "Go sports! #Sports"
result = tweet.split('#')[1]
print(result)

print('x' in [1, 2, 3, 'x'])


# Some exercises to sharpen the brain
def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


print(arrayCheck([1, 2, 3, 4, 5, 6]))


def stringBits(mystring):
    result = ""
    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i]
    return result


print(stringBits("hello"))


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]


print(end_other('bill', 'ill'))
