# def hello(name="Bill"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME()"
#     if name == "Bill":
#         return greet
#     else:
#         return welcome
#
#
# x = hello()
# print(x())

# def hello():
#     return "Hi Bill!"
#
#
# def other(func):
#     print("HELLO")
#     print(func())
#
#
# other(hello)


def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
