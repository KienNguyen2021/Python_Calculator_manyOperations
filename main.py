#Calculator helps users to use many times before exit

#Add :
def add(n1, n2) :
  return n1 + n2

#Subtract :
def subtract(n1, n2) :
  return n1 - n2

#Multiply :
def multiply(n1, n2) :
  return n1 * n2

# Divide :
def divide(n1, n2) :
  return n1 / n2  

#Dictionary in Function :

operations = {
  "+" : add,
  "-"  : subtract,
  "*"  : multiply,
  "/"  :  divide,
}


#def calculator() :

num1 = int(input(" What is the first number :?\n "))
  

# Use For Loop to print out each symbol in the dictionary :

for symbol in operations :
     print(symbol)

# Use While loop to continue the calculato :

should_continue = True

while should_continue :

    operation_symbol = input("Pick an operation from the line above : ")  
    num2 = int(input("What is the next number :? "))
    calculation_function = operations[operation_symbol]

    answer = calculation_function (num1, num2)   # pass num1, num2

    print(f"{num1}{operation_symbol}{num2} = {answer}")

    if input(f" Type 'y'to continue calculating with {answer}, or type 'n' to exit.") == "y":
  
      num1 = answer

    else :
      
      should_continue = False

     # calculator ()

#calculator()