

# Prints the index of the number from a list if in list, else prints -1
def find_index(list, start, finish, number):
    if list[finish-1] < number or list[start] > number:
            print("-1")
    else:
        mid =  (start + finish) // 2
        if number == list[mid]:
            print(mid)
        elif number < list[mid]:
            find_index(list, start, mid, number)
        else:
            find_index(list, mid + 1, finish, number)

 # Read the number and the list and returns the index of the number in the list       
def get_index_from_file():
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
    return find_index(ordered_list, 0, len(ordered_list), given_number)

    

get_index_from_file()