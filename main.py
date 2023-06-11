import operator
from collections import Counter
"""
Task №1
In this task you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.
"""
def filter_list(lst):
    return [el for el in lst if isinstance(el, int)]

"""
Task №2
Write a function named 'first_non_repeating_letter' that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
"""
def first_non_repeating_letter(string):
    t = string.lower()
    freq = Counter(t)
    for ch in t:
        if (freq[ch] == 1):
            return ch
            break

"""
Task №3 
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more 
than one digit, continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.
"""
def digital_root(n):
    total = sum([int(num) for num in str(n)])
    if len(str(total)) >= 2:
        sums = digital_root(total)
    return total

"""
Task №4
There is an array of numbers - arr [1, 3, 6, 2, 2, 0, 4, 5] 
there is a number target = 5.
Count the number of pairs in the array, the sum of which will give target
"""
def target_pairs(arr, target):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if i + j == target:
                print(i, ' + ', j, ' = ', i+j)
                return

    print("No pairs")

"""
Task №5
Den has invited some friends. His list is:

s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that
· makes this string uppercase
· gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result
between parentheses separated by a comma.
"""
def sort_guest_list(s):
    s = s.upper()
    guest_list = s.split(';')
    formatted_list = []

    for entry in guest_list:
        names = entry.split(':')
        first_name = names[0]
        last_name = names[1]

        formatted_list.append((last_name, first_name))

    sorted_list = sorted(formatted_list, key=lambda x: (x[0], x[1]))

    result = ''
    for entry in sorted_list:
        last_name, first_name = entry
        result += f"({last_name}, {first_name}) "

    return result.strip()


if __name__ == '__main__':
    #Task 1
    input = [25, "some", "useless", 30, "text", 11, 12]
    filtered = filter_list(input)
    print(filtered)

    #Task 2
    str_input = "AbaBbc"
    print(first_non_repeating_letter(str_input))

    #Task 3
    n = 99
    print(digital_root(n))

    #Task 4
    num_arr = [1, 2, 4, 6, 8]
    target = 7
    target_pairs(num_arr, target)

    #Task 5
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    sorted_guests = sort_guest_list(s)
    print(sorted_guests)





