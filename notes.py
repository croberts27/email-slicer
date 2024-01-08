# A method is similar to a function. A method is tied to a specific data type

# x = "happy birthday"
#
# index = x.index("birtdhay")
# print(index)
# returns 6

# x = "happy birthday"
#
# index = x.find("aSDFLLDSJKF")
#
# print(index)
# returns -1. Find method doesn't return an error. this means the arg doesn't exist

# x = "0000000happybirthday00000"
#
# x = x.strip("0") # strips arg
# x = x.lstrip("0") # strips arg on the left
# x = x.rstrip("0") # stirps arg on the right
# print (x)

# name = input("What is your name?: ")
# print(name)
# len(name) # gives us 4 since it is taking in the question as an index
# name = input("What is your name?: ").strip() # only takes in index of user input
# print(name)
# len(name) # len will give us index length of user input

# HOW TO SLICE
# word = "hellomynameiscalvin"
# variable = var[start:end:step] end is the letter you go up to but not include
# slice = word[0:5:1]
# print (slice) this prints hello
# Step is the number of indexes python moves to return your slice
# slice = word[0:5:2] returns hlo

# word = "supercalifragilisticexpialidocious"
# # todo create slice that takes out word 'cali'
# # slice = word[5:9:1]
#
# slice = word[word.index("cali"):word.index("fragi")]
# print(slice) returns cali