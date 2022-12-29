# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
#EASY WAY--------------------------------------------------------------
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

passwordLetterString = ""
passwordNumberString = ""
passwordSymbolString = ""


for letter in range(1,nr_letters + 1):
  passwordLetterString += random.choice(letters)
#print(passwordLetterString)

for symbol in range(1,nr_symbols + 1):
  passwordSymbolString += random.choice(symbols)
#print(passwordSymbolString)

for number in range(1,nr_numbers + 1):
  passwordNumberString += random.choice(numbers)
#print(passwordNumberString)

print(f"\n{passwordLetterString}{passwordSymbolString}{passwordNumberString}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Password Generator Project
#HARD WAY--------------------------------------------------------------
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\nWelcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

passwordString = ""
combinedList = []

for letter in range(1,nr_letters + 1):
  combinedList.append(random.choice(letters))
#print(combinedList)

for symbol in range(1,nr_symbols + 1):
  combinedList.append(random.choice(symbols))
#print(combinedList)

for number in range(1,nr_numbers + 1):
  combinedList.append(random.choice(numbers))
#print(combinedList)

#print(combinedList)

random.shuffle(combinedList)

#print(combinedList)

for element in range(0, len(combinedList)):
  passwordString += combinedList[element]
  
print(f"\n{passwordString}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P