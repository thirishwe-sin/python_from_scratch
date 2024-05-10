def greet(fun):

    def wrapper(name):
        #before
        print('hello')
        fun(name)
        #after
        print('good byr')

    return wrapper
    
@greet
def sayName(name):
    print(name)

sayName('hlaing min than')