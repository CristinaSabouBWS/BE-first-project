import pdb
#Print the Nth number in the Fibonacci sequence (google for rule). 0 <= N <=1 000 000
def fibonacci_recursive(number):
    if number == 0:
        return(0)
    elif number == 1:
        return(1)
    else:
        return(fibonacci_recursive(number-1) + fibonacci_recursive(number -2))

def fibonacci_iterative(number):
    fib_list = [0] * (number+1) 
    fib_list[1] = 1
    for i in range(2, number+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[number]

def read_number():
    number = int(input("Give a number greater than 0 and smaller than 1 000 000: "))
    if number < 0 or number > 1000000:
        number = int(input("You gave a number out of range. Give a number greater than 0 and smaller than 1 000 000: "))
    return(number)

def print_fibo():
    print("Fibonacci exercise")
    number = read_number()
    print(f"Recursive is simpler: {fibonacci_recursive(number)}")
    print(f"iterative is more efficient: {fibonacci_iterative(number)}")

#2. Find all the divisors of a number
def divisors(n):
    divisors =[1]
    for i in range(2, int(n/2) +1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def print_divisors():
    print("Divisors exercise")
    number = read_number()
    print(f"List o divisors for {number}: {divisors(number)}")

#Given a file with 2 sorted lists of integers (each list on its row), 
#print a single list with all of the elements from the input lists, such that the single list is also sorted. 
#Hint: you should not use any sort function here, but rely on the property of the inputs.
def combine(sorted_list_1, sorted_list_2):
    combined_list = []
    i = j = 0
    while i < len(sorted_list_1) and j < len(sorted_list_2):
        if sorted_list_1[i] < sorted_list_2[j]:
            combined_list.append(sorted_list_1[i])
            i +=1
        else:
            combined_list.append(sorted_list_2[j])
            j +=1
    while i < len(sorted_list_1):
        combined_list.append(sorted_list_1[i])
        i += 1
    while j < len(sorted_list_2):
        combined_list.append(sorted_list_2[j])
        j += 1
    return combined_list

def combined_sorted_list():
    f = open("input_sorted_list.txt", "r")
    sorted_string_1 = f.readline()
    sorted_string_2 = f.readline()
    sorted_string_1 = sorted_string_1.strip()
    sorted_string_1 = sorted_string_1.split(" ")
    sorted_string_2 = sorted_string_2.split(" ")
    sorted_list_1 = []
    sorted_list_2 = []
    for i in sorted_string_1:
        sorted_list_1.append(int(i))
    for i in sorted_string_2:
        sorted_list_2.append(int(i))

    combined_list = combine(sorted_list_1, sorted_list_2)
    print(f"Combined lists: of {sorted_string_1} + {sorted_string_2}:")
    print(combined_list)



if __name__ == "__main__" :
   
    print_fibo()
    print_divisors()
    combined_sorted_list()