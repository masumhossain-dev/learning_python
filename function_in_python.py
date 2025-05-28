#its work like void function, is hasen't any return and paramiter.
def func():
    a = 10
    b = 20
    print(a+b)


func()

#function with paramiter in python
def adder(a, b):
    print(a+b)

adder(10, 20)

#with return
def multi(a, b):
    return a*b

print(multi(10, 3))


#return without params
def add():
    return 10+20

print(add())