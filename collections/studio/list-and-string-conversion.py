proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for s in strings:
 if "," in s:
    print(f"The strings {s} are seperated by commas.")
 elif ";" in s:
    print(f"The strings {s} are seperated by semicolon.")
 elif " " in s:
    print(f"The strings {s} are seperated by space.")
 else:
    print(f"The string {s} has an unknown delimiter.")

# b) If the string uses commas to separate the words, split it into an array, 
# reverse the entries, and then join the array into a new comma separated string.

for s in strings:
 if "," in s:
    words = s.split(',')
    words.reverse()
    commaSeparatedReverseString = ','.join(words)
    print("Comma separated reverse string: " + commaSeparatedReverseString)
# c) If the string uses semicolons to separate the words, split it into an array, 
#  the entries, and then join the array into a new comma separated string.
for s in strings:
 if ";" in s:
   words = s.split(';')
   commaSeparatedString = ','.join(words)
   print("Comma separated string: " + commaSeparatedString)

# d) If the string uses spaces to separate the words,
#  split it into an array, reverse alphabetize the entries, 
# and then join the array into a new space separated string.
for s in strings:
 if " " and not "," in s:
   words = s.split(" ")
   words.sort(reverse=True)
   spaceSeparatedString = ' '.join(words)
   print("Space separated reverse alphabetized string: " + spaceSeparatedString)



# e) If the string uses ‘comma spaces’ to separate the list,
#  modify your code to produce the same result as part “b”,
#  making sure that the extra spaces are NOT part of the final string.
for s in strings:
 if ", " in s:
    words = s.split(', ')
    words.reverse()
    commaSpaceSeparatedReverseString = ','.join(words)
    print("Comma-Space separated reverse string - no extra spaces: " +     commaSpaceSeparatedReverseString)
