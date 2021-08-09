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

def convertWageMtoW(mWage):

   wageGap = 0.182

   ratio = 1 - wageGap

   return mWage * ratio

# test cases (given from assignment)   
print(convertWageMtoW(100))
print(convertWageMtoW(76.2))
print(convertWageMtoW(0))

# own test cases
print(convertWageMtoW(34))
print(convertWageMtoW(94))


userNumber = getNumber()
print(userNumber)
print("summed up: ", sumDigits(502))

x = sumTwo(3,5)

print(x)
