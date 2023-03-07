from functions import calculate

print("Hello world")

print("Enter number_1")
num1 = float(input())
print("Enter number_2")
num2 = float(input())
print("Enter operation(add, sub, mult, div)")
operator = input()
result = calculate(num1, num2, operator)
print("Reuslt: " + str(result))