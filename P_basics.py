# price = 10
# rating = 4.9  # float
# name = 'meher'
# is_published = True  # boolean
# print(price)

# name1 = 'john smith'
# age = 20
# is_new = True
# print(name1)
# print(f"Name: {name1}, Age: {age}, New Patient: {is_new}") # f-string

#name = input('what is your name? ')
#print('Hi ' + name)
#color = input('what is your favourite color? ')
#print(name + ' likes ' + color)

#birth_year = input('birth year: ')
#print(type(birth_year))
#age = 2024 - int(birth_year)
#print(type(age))
#print(age)

# weight = input('what is your weight in pounds? ')
# in_kg = float(weight) * 0.454 # changes the string into float or else the code won't run
# print(f"{in_kg} kg") # adds Kg with the value

# course = 'python for beginners'
# print(course[0])  # prints the first character
# print(course[-1])  # prints the last character
# print(course[0:])  # prints all the characters
# print(course[1:])  # prints all the characters except for the first
# another = course[:]
# print(another)
# name = 'jennifer'
# print(name[1:-1])  # prints from the second to last char, excluding the last char

# first = 'john'
# last = 'smith'
# msg = f'{first} + [{last}] is a coder'  # formatted string
# print(msg)

# print(len(course))  # len function counts the number of chars in a string.
# len can also count the number of items in a list
# print(course.upper())  # changes all the chars to upper case
# print(course.lower())  # changes all the chars to lower case
# print(course.find('beginners'))  # finds and prints the index where beginner start , case sensitive
# print(course.replace('beginners', 'absolute beginners'))  # creates a new string with a replaced word, case sensitive
# print('java' in course)  # in function creates a boolean expression
# print(10 + 2)  # add
# print(10 - 2)  # subtract
# print(10 / 2)  # divide
# print(10 // 2)  # divide and changes to an integer
# print(10 % 2)  # modulo gives the reminder# print(10 * 2)  # multiple
# print(10 ** 2)  # to the power
# x = 10
# x = x + 2
# x += 2  # augment operator , also increases the value
# print(x)
# y = (10 + 3) * 2 ** 2
# print(y)
# z = (2 + 3) * 10 - 3  # operator precedence , BODMAS
# print(z)

#  m = 2.9
# print(round(m))  # rounds the value
# print(abs(m))  # absolute function always returns positive value

# import math
# print(math.ceil(2.9))  # ans is 3
# print(math.floor(2.9))  # ans is 2

# is_hot = False  # capital F for false
# is_cold = False

# if is_hot:
#    print("it's a hot day")
#    print("drink plenty of water")
#elif is_cold:  # elif is else if in python
#    print("it's a cold day")
#    print("wear warm clothes")
#else:
#    print("it's a lovely day")

#print("enjoy your day")

#price = '100000'
#good_credit = True

#   down_pay = float(price) * 0.1
#else:
#    down_pay = float(price) * 0.2
#print(f"down_pay: ${down_pay}")

#has_high_income = True
#has_good_credit = False
#if has_high_income and has_good_credit:  # logical operator 'and'
#    print("Eligible for loan")

#if has_high_income or has_good_credit:  # logical operator 'or'
#    print("Eligible for loan")

#name = "meher"
#if len(name) < 3:
#    print("Name must be at least 3 characters")
#elif len(name) > 50:
#    print("Name must be a maximum of 50 characters")
#else:
#    print("Name looks good !")

#weight = float(input('what is your weight? '))
#unit = input(' (L)bs or (K)g: ')
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print( f"You are {converted} kilos")
#else:
#    converted = weight/ 0.45
#    print(f"You are {converted} pounds")

#i = 1
#while i <= 5:
#    print('*' * i)
#    i = i + 1

#secret_number = 10
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
#    guess = int(input('Guess: '))
#    guess_count +=1
#    if guess == secret_number:
#        print("You won!")
#        break
#else:
#    print('Sorry, you failed!')

#need_help = input('Need help? : ')
#print(f'start - to start the car \n stop - to stop the car \n quit - to exit')

#for item in 'python':
 #   print(item)

#   print(item)

#    print(item)

#prices = [10, 20, 30]

#  total += price
#print(f"Total: {total}")

#   for y in range(3):
 #       print(f'({x}, {y})')

#numbers = [5, 2, 5, 2, 2]
#for number in numbers:
#    print(number * 'x')

#nums = [5, 2, 5, 2, 2]
#for x_count in nums:
#    output = ''
#    for count in range(x_count):
#    print(output)

    #lists
# names = ['john', 'bob', 'mosh', 'sarah']
# print(names[2:])   # prints from index 2 to the last index
# names[0] = 'jon'    # Prints the value of the first index
# print(names)        # prints the whole list
# print(names[1] == 'bob') # create a boolean and returns true

# num_list = [1, 2, 3, 4, 5]
# largest_num = 0    # assigns the value of the largest number to zero
# for num in num_list:   # goes through the list
#    if num > largest_num:  # if the current number is greater than the largest number
#        largest_num = num  # assigns that number to be the largest
# print(largest_num)

# matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#   [7, 8, 9]
#]
#matrix[2][2] = 20
#print(matrix[2][2])

#   for item in row:
#NUMBERS = [5, 6, 7, 8, 9, 6, 9]
#NUMBERS.append(20)  # adds a number to the end of the list
#NUMBERS.insert(1, 4)  # inserts a value anywhere in the list
#NUMBERS.remove(7)
# NUMBERS.clear()  # removes all values
#print(NUMBERS)
#print(50 in NUMBERS)  # finds 50 in the list
#print(NUMBERS.count(5))  # counts the number of 5s in the list
#NUMBERS.sort()  # sorts in ascending order , small to big
#NUMBERS.reverse()  # sorts in descending order , big to small
#print(NUMBERS)

#no_duplicate = list(set(NUMBERS))  # sets in python cannot have duplicates
#print(no_duplicate)

#unique = []  # new empty list
#for number in NUMBERS:
 #   if number not in unique:
 #       unique.append(number)
#print(unique)

#coordinates = (1, 2, 3)  # unpacking of tuples , can also be done lists
#x, y, z = coordinates
#print(y)

# Dictionaries
# store information as key, value pairs
# keys should be unique

# customer = {
#    "name": "john smith",
#    "age": 30,
 #   "is_verified": True
# }
# print(customer.get("age"))  # to find a key and return its value
# print(customer.get("age", "30"))  # to find a key value pair
# customer["name"] = "jack smith"  # updating value for a key
# print(customer["name"])

#phone_number = {
#    int(1): "One",
#    int(2): "Two",
#    int(4): "Four",
#}
#print(phone_number[1])
#print(phone_number[2])
#print(phone_number[3])
#print(phone_number[4])


#message = input(">")
#words = message.split(' ')
#emojis = {
#  ":(" : "😔"
#}
#output = ""
#for word in words:
#    output += emojis.get(word, word) + " "
#   print (output)
# Functions
#def greet_user():
#    print('Hi there!')
#    print('Welcome aboard')


#print("Start")
#greet_user()
#print("Finish")


# Parameters
#def greet_user(first_name, last_name):
#    print(f'Hi {first_name} {last_name}!')
#    print('Welcome aboard')


#print("Start")
#greet_user("John", "Smith")
#print("Finish")


#def square(number):
#    return (number * number)


#print(square(3))

#try:
 #  income = 20000
 #   risk = income / age
 #   print(age)
#except ZeroDivisionError:
 #   print('Age cannot be zero.')
#except ValueError:
 #   print('Invalid value')


#class Point:
#   def move(self):
#        print("move")

#    def draw(self):
#        print("draw")


#point1 = Point()
#point1.x = 10
#point1.y = 20
#print(point1.x)
#point1.draw()


#class Person:
#    def __init__(self, name):  # constructor method
#        self.name = name

#    def talk(self):
#        print(f"Hi, I am {self.name}")


#john = Person("John Smith")  # creates an instance of the person class
#john.talk()
#bob = Person("Bob Smith")
#bob.talk()


#   def walk(self):
#        print("walk")


#class Dog(Mammal):
#    def bark(self):  # you could also write pass if you want to leave the class empty
#        print("bark")


#class Cat(Mammal):
#    def Be_annoying(self):
#        print("cat is annoying")


#dog1 = Dog()
#dog1.walk()
#cat1 = Cat()
#cat1.Be_annoying()

