from functions import calculate

print("Hello world")

try:
    print("Enter numbers and operator")
    num1 = float(input())
    print("Enter number_2")
    num2 = float(input())
    print("Enter operation(add, sub, mult, div)")
    operator = input()
    result = calculate(num1, num2, operator)
    print("Reuslt: " + str(result))
except Exception as exp:
    print(exp.args)
    


numbers = [1,2,3,4,5,6,7,8,9,10]

print("\nList")
for n in numbers:
    print(n)

print("Even List")
for i in range(len(numbers)):
    if(numbers[i]%2 == 0):
        print(numbers[i])