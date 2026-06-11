#Day2
#If statement
#Python Calculator
print("Welcome to the Python Calculator!")
#python calculator that can perform basic arithmetic operations 
num1 = float(input("Enter number 1: "))
operator= input("Enter the operator (*,+,- and /): ")
num2= float(input("Enter number 2: "))

if operator== '*':
    result1 = num1*num2
    print(f"The result is {result1}")
elif operator == '/':
    result2 = num1/num2
    print(f"result is: {result2} ")
elif operator == '+':
    result3 = num1+num2
    print(f"result is: {result3} ")
elif operator == '-':
    result4 = num1-num2
    print(f"result is: {result4} ")
else:
    print("Enter a valid operator(+,-,*,or /): ")