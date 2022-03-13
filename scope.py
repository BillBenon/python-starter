# LOCAL
lambda x: x ** 2

# Enclosing function locals
name = 'This is a global name!'


def greet():
    name = "Bill"

    def hello():
        print("Hello " + name)

    hello()


greet()

x = 50


def func():
    global x
    x = 1000
    return x


print("Before function call, x is: ", x)
func()
print("After function call, x is: ", x)
