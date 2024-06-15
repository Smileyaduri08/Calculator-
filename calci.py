def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers, handling division by zero."""
  if y == 0:
    return "Error: Cannot divide by zero."
  else:
    return x / y

while True:
  # Get user input
  print("Enter first number: ")
  num1 = float(input())
  print("Enter operator (+, -, *, /): ")
  operator = input()
  print("Enter second number: ")
  num2 = float(input())

  # Perform calculation based on operator
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")
    continue

  # Print result
  print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to continue
  print("Do you want to continue? (y/n): ")
  choice = input()
  if choice.lower() != "y":
    break

print("Calculator closing...")
