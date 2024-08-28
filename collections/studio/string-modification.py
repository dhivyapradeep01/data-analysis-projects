my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
print(my_string[3:] + my_string[:3])

# Use a template literal to print the original and modified string in a descriptive phrase.
modified_string = my_string[3:] + my_string[:3]
print(f"The original string is {my_string} and the modified string is {modified_string}.")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
num_letters = int(input("How many letters to relocate?"))
if num_letters > len(my_string):
 print(f"The number is larger than {my_string}")
else:
  relocate_letters = my_string[:num_letters]
  remaining_letters = my_string[num_letters:]
  new_string = remaining_letters + relocate_letters
  print(f"The new string is:{new_string}")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
num_letters = int(input("How many letters to relocate? "))
if num_letters > len(my_string):
 num_letters = 3
 print(f"The number is larger than the length of the string. Defaulting to moving 3 characters.")
relocate_letters = my_string[:num_letters]
remaining_letters = my_string[num_letters:]
new_string = remaining_letters + relocate_letters
print(f"The new string is: {new_string}")