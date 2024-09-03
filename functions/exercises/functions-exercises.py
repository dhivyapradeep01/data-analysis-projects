# Part 1 A -- Make a Line
def make_line(size):
   line = ""
   for i in range(size):
      line += "#"
   return line

print(make_line(5))
print ("Done making a Line \n\n")

# Part 1 B -- Make a Square
def make_square(size):
    line = ""
    squarePrint = ""
    for i in range(size):
        line += "#"
    squarePrint = squarePrint + line
    for i in range(size-1):
        squarePrint = squarePrint + "\n" + line
    return squarePrint

print(make_square(5))
print ("Done making a Square without calling another function \n\n")
# create a function using your make_line function to code a square
def make_square(size):
    line = ""
    squarePrint = ""
    line = make_line(5)
    squarePrint = squarePrint + line
    for i in range(size-1):
        squarePrint = squarePrint + "\n" + line
    return squarePrint

print(make_square(5))
print ("Done making a Square calling make_line function \n\n")


# Part 1 C -- Make a Rectangle
def make_rectangle(width, height):
   rectangle = ""
   for i in range(height):
      rectangle += (make_line(width) + "\n")
   return rectangle

print(make_rectangle(5, 3))
print ("Done making a rectangle\n\n")

# Make Square Using rectangle functions

def make_square_with_rect(size):
    squarePrint = ""
    squarePrint = make_rectangle(size, size)
    return squarePrint

print(make_square_with_rect(5))
print ("Done making a square using rectangle function. The rectangle funtion had be be defined before being called\n\n")


# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
   stairs = ""
   for i in range(height):
      stairs += (make_line(i+1) + "\n")
   return stairs

print(make_downward_stairs(5))

print ("Let's run down the stairs.\n\n")


# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChars):
    space_line=""
    for i in range(numSpaces):
        space_line = space_line +" " 
    for i in range(numChars):
        space_line = space_line +"#" 
    for i in range(numSpaces):
        space_line = space_line +" " 

    return space_line

print(make_space_line(3, 5));
print ("Done making space line\n\n")


# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
   triangle = ""
   for i in range(height):
      triangle += (make_space_line(height - i - 1, 2 * i + 1) + "\n")
   return triangle

print(make_isosceles_triangle(5))
print ("Done making Isosceles Triangle\n\n")

# Part 3 -- Make a Diamond

def make_diamond(height):
   diamond = ""
   triangle = make_isosceles_triangle(height)
   diamond += triangle[:-1]
   for i in range(len(triangle)-1, -1, -1):
      diamond += triangle[i]
   return diamond

print(make_diamond(5))
print ("Whoa! look at the size of that diamond! :) \n\n")