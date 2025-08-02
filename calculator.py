# Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(a, "+", b, "=", a + b)
elif op == "-":
    print(a, "-", b, "=", a - b)
elif op == "*":
    print(a, "*", b, "=", a * b)
elif op == "/":
    if b != 0:
        print(a, "/", b, "=", a / b)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")
