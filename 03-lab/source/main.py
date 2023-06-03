import math
from Serializers.json_serializer import JsonSerializer
from Serializers.xml_serializer import XmlSerializer
from Serializers.converter import Converter

def my_decor(meth):
    def inner(*args, **kwargs):
        return meth(*args, **kwargs) + 1

    return inner

class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass



C_ser = XmlSerializer.dumps(C)
C_des = XmlSerializer.loads(C_ser)

c = C(1, 2)
c_ser = XmlSerializer.dumps(c)
c_des = XmlSerializer.loads(c_ser)


print(c.my_sin(10))

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())


def f(a):
    for i in a:
        yield i


g = f([1, 2, 3])
print(next(g))
g_s = XmlSerializer.dumps(g)
g_d = XmlSerializer.loads(g_s)
print(next(g_d))


def a(x):
    yield x[0]
    x[1] += 2
    yield



lambda_function = lambda x: (x ** x) // 3
s_lf = XmlSerializer.dumps(lambda_function)
d_lf = XmlSerializer.loads(s_lf)

print(lambda_function(10))
print(d_lf(10))

def recursion_func(x):
    if x < 2:
        return 1
    return recursion_func(x - 1) * x

s_rf = XmlSerializer.dumps(recursion_func)
d_rf = XmlSerializer.loads(s_rf)

print(recursion_func(15))
print(d_rf(15))



def max_arguments(max_count):
    def decorator(func):
        def wrapper(*args):
            if len(args) <= max_count:
                return func(*args)
            else:
                print("Limit was reached")
        return wrapper
    return decorator

@max_arguments(3)
def print_arguments(*args):
    for arg in args:
        print(arg)


print_arguments('Hello', 'world', 123)  
print_arguments('Hello', 'world', 123, [1, 2, 3]) 

def increase_int_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            result += 3
        return result
    return wrapper


@increase_int_result
def calculate(x, y):
    return x + y

@increase_int_result
def get_length(s):
    return len(s)

print(calculate(5, 7))
print(get_length("Hello"))



class Manager:
    def __enter__(self):
        print("Hello")


    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print("GoodBye")

        return True
    

with Manager() as dv:
    a = 5/0

