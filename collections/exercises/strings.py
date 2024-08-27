# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

print(text[:12])
# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[:-12])

# 3. Print a slice of the middle 12 characters from 'text'.
#Calculate first and second
print("-->Calculate the middle 12 characters instead of manually doing it:<--")
lenOfText = len(text)
firstLen = (lenOfText/2)-6
secondLen =  (lenOfText/2)+6
print(text[int(firstLen):int(secondLen)])
#print manually
print("-->Print middle 12 manually<--")
print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
print("-->Looping:Print 1 letter per line<--")
max_index = len(word)-1
for index in range(max_index, -1, -1):
   print(word[index])


# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.

print("-->Looping:Accumulator Pattern<--")
new_word = ""
for index in range(max_index, -1, -1):
   new_word += word[index]

print(new_word)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').

print("-->Looping:Original + Reversed<--")
new_word_original = ""
new_word_reversed = ""
max_index_loop = len(word)
for index in range(max_index_loop):
   new_word_original += word[index]

for index in range(max_index, -1, -1):
   new_word_reversed += word[index]

print(new_word_original + "|"+ new_word_reversed)