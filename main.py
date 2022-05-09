

# Open input.txt to read lines
f = open("input.txt", "r")

# Read the first line to a number
given_number = int((f.readline()))

# Read second line to a list of strings by splitting the line
second_line = (f.readline())
ordered_list = second_line.split(" ")

# Converting the list of strings to a list of integers
for i in range(0, len(ordered_list)):
    ordered_list[i] = int(ordered_list[i])


print(ordered_list)

# In progress
if ordered_list[-1] < given_number or ordered_list[0] > given_number:
        print("-1")
else:
    mid = ordered_list[round(len(ordered_list) / 2)]
    if given_number == mid:
        print(ordered_list.index(mid))
    

