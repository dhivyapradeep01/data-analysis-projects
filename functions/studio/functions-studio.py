# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
# e) Create a variable of type string to test your new function. 
# # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.

def reverse_characters(string_input):
    return ''.join(reversed(list(string_input)))

test1 ='apple'
test2 ='LC101'
test3 ='Capitalized Letters'
test4 ='I love the smell of code in the morning.'
print (reverse_characters(test1))
print (reverse_characters(test2))
print (reverse_characters(test3))
print (reverse_characters(test4))
print ("---------------------------")

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

def reverse_characters(input_value):
    if isinstance(input_value, str):
        # Reverse the string using reversed() and join()
        return ''.join(reversed(list(input_value)))
    elif isinstance(input_value, int):
        # Convert the integer to a string, reverse it, and convert back to an integer
        reversed_str = ''.join(reversed(list(str(input_value))))
        return int(reversed_str)

# Test cases
test_num1 = 1234
test_str1 = 'LC101'
test_num2 = 8675309
test_str2 = 'radar'

# Print results
print(reverse_characters(test_num1))  
print(reverse_characters(test_str1))  
print(reverse_characters(test_num2))  
print(reverse_characters(test_str2)) 
print ("---------------------------")

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.

def reverse_list_elements(input_list):
    # a) Define and initialize an empty list
    reversed_list = []
    
    # b) Loop through the old list
    for item in input_list:
        # c) For each element, call reverse_characters to flip the characters or digits
        reversed_item = reverse_characters(item)
        # d) Add the reversed string (or number) to the new list
        reversed_list.append(reversed_item)
    
    # e) Return the final, reversed list
    return reversed_list


list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
# Print results for each test case
print("Test case 1 (strings only):")
print(reverse_list_elements(list_test1))

print("\nTest case 2 (numbers only):")
print(reverse_list_elements(list_test2))

print("\nTest case 3 (numbers and strings):")
print(reverse_list_elements(list_test3))

print ("---------------------------")