import math
from Serializers.json_serializer import JsonSerializer

class A:
	def my_method(self):
		return 5

class B:
	def another_method(self):
		return 6

class C(A, B):
	pass

x = 10
def my_func(a):
	return math.sin(x * a)

obj = C()
ser_obj = JsonSerializer.dumps(obj)
deser_obj = JsonSerializer.loads(ser_obj)
print(deser_obj.my_method()) # returns 5
print(deser_obj.another_method()) # returns 6

ser_class = JsonSerializer.dumps(C)
deser_class = JsonSerializer.loads(ser_class)
obj = deser_class()
print(obj.my_method()) # returns 5
print(obj.another_method()) # returns 6

ser_func = JsonSerializer.dumps(my_func)
deser_func = JsonSerializer.loads(ser_func)
print(deser_func(20)) # returns sin(10 * 20)
