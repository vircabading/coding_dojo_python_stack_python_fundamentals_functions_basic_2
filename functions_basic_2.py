# /////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > Fundamentals: Functions Basic 2
# By:   Virgilio D. Cabading Jr.    Created: Oct 25, 2021
# /////////////////////////////////////////////////////////////

def print_desc(description) :
    print()
    print("////////////////////////////////////////////////////////////////////////////")
    print(description)
    print()

# /////////////////////////////////////////////////////////////
print_desc("1. Countdown")

def countdown(high_number) -> list:
    list_output = []
    for idx in range (high_number, -1, -1):
        list_output.append(idx)
    return list_output

print(countdown(5))

# /////////////////////////////////////////////////////////////
print_desc("2. Print and Return")

def print_and_return(number_list):
    print (f"printing first number in list: {number_list[0]}")
    return number_list[1]

print("Number returned from print_and_return([1,2]) is", print_and_return([1,2]))

# /////////////////////////////////////////////////////////////
print_desc("3. First Plus Length")

def first_plus_length (number_list):
    sum = 0;
    if len(number_list) > 0 :
        sum += number_list[0]
    return sum + len(number_list)

print ("first_plus_length of [1,2,3,4,5] is", first_plus_length([1,2,3,4,5]))

"""
# /////////////////////////////////////////////////////////////
print_desc("4.")

# /////////////////////////////////////////////////////////////
print_desc("5.")

"""