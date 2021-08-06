# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c

# modify this function to repeat

def getNumber():
  
  finalnumber = " "
  
  symbols = input("Enter a digit: ")
  
  number = int(symbols)
  
  while number != -1:
    finalnumber = finalnumber + str(number)
    
    symbols = input("Enter a digit: ")
    
    number = int(symbols)
  
  return finalnumber

userNumber = getNumber()
print(userNumber)

x = sumTwo(3,5)

print(x)
