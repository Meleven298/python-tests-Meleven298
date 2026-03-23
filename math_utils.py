def add(a,b):
    arguments_checking(a,b)

    return a+b
    
def substract(a,b):
    arguments_checking(a,b)

    return (a-b)

def multiply(a,b):
    arguments_checking(a,b)

    return a*b

def divide(a,b):
    arguments_checking(a,b)

    if b != 0:
        c = a/b
    else:
        raise ZeroDivisionError('На ноль делить нельзя')

    return c

def arguments_checking(a,b):
    if not (isinstance(a, (int, float)) and isinstance(b,(int,float))):
        raise TypeError('Аргументы должны быть типа int или float')
    