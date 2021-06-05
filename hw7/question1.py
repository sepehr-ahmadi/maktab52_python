from num2words import num2words
def remainder(*args,**kwargs):
    def inner_function(func):
        def output():
            res=func()%int(args[0])
            return res
        return output
    return inner_function
def string_p(func):
    def inner_function():
        return num2words(func())
    return inner_function
def cache():
    pass



#@string_p
@remainder(5)
def product():
    first_number=int(input("please enter first number:\n"))
    second_number=int(input("please enter second number:\n"))
    return first_number*second_number
print(product())