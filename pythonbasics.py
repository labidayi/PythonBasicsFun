import math 
import csv
"""
this is
a multi
line comment
"""

x = 10
if x == 5:
    print("x is 5")
elif x == 7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

for character in "python":
    print(character)

for i in range(0, 5, 1):
    print(i)
for i in range(5):
    print(i)
for i in range(0, 5):
    print(i)

for i in range(2, 42, 2):
    print(i, end=" ")
print()

i = 2
while i <= 40:
    print(i, end=" ")
    i += 2

def say_hello():
    print("hello")

for i in range(10):
    say_hello() # call

# example #2
# function with one input and no
# return
def say(message):
    print(message)

say("hi!!")
say("how are you??")
say("goodbye...")

# example #3
# function with one input
# and one return (output)
def compute_circle_area(radius):
    area = math.pi * radius ** 2
    return area # send back to
    # calling code

result = compute_circle_area(5)
print("result:", result)


list_ints = [10, 4, -2, 9]
print(list_ints)
print(list_ints[1], list_ints[-3])

# lists are mutable
# (they can be changed)
list_ints[0] = 4000
print(list_ints)

# items in a list can have mixed type
list_ints[-1] = "hello"
print(list_ints)

print(len(list_ints))
# add another item
list_ints.append(42) # adds to end
print(len(list_ints))

empty_list = []
print(len(empty_list))

nested_list = [[0, 1], [2, 3], [], [8]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][1])

# looping through list items
cities = ["hangzhou", "beijing", "shanghai"]
for city in cities:
    print(city)
print()
# task: try writing the above for loop
# using a while loop
i = 0
while i < len(cities):
    print("i:", i, "cities[i]:", cities[i])
    i += 1

# common list operators
print(cities)
# list concatenation +=
# adding 2 lists together
cities += ["shenzhen", "chongqing"]
print(cities)
# list repetition * 
# repeating items in a list
repeated_list = 3 * ["guangzhou", "tianjin"]
print(repeated_list)

print(cities)
print(cities[1:3])

print(cities[:2]) # start is 0
print(cities[2:]) 
cities_copy = cities[:]
print("copy:", cities_copy)
cities_copy[0] = "HANGZHOU" 
print("copy:", cities_copy)
print("original:", cities)

cities.append("new york city")
print(cities)
# remove() delete item based on value
cities.remove("shanghai")
print(cities)
# pop() delete item based on index
cities.pop(-1)
print(cities)

string_list = ["new", "york", "city"]

one_string = "***".join(string_list)
print(one_string)

comma_separated_value_string = "new,york,city"

sl2 = comma_separated_value_string.split(",")
print(sl2)

star_separated_value_string = "new***york***city"
sl3 = star_separated_value_string.split("***")
print(sl3)

filename = "data.csv"
infile = open(filename, "r") 
reader = csv.reader(infile)
table = []
for row in reader:
    print(row) 
    table.append(row)
# 3. close the file
infile.close()

print("after closing file, table:")
print(table) 
header = table.pop(0)
print("header:", header)
print("table:")
print(table)
