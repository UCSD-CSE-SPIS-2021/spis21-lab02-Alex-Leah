# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c

# modify this function to repeat

def getNumber():
  
  finalnumber = ""
  
  symbols = input("Enter a digit: ")
  
  number = int(symbols)
  
  while number != -1:
    finalnumber = finalnumber + str(number) 
    
    symbols = input("Enter a digit: ")
    
    number = int(symbols)
  
  return finalnumber

def sumDigits(x):

   # You will need to complete this function
   sum = 0

   while x != 0 :
     sum = sum + x % 10
     x = x // 10

   return sum

userNumber = getNumber()
print(userNumber)
print("summed up: ", sumDigits(502))

x = sumTwo(3,5)

print(x)
