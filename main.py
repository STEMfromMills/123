#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" 
pear_image = "pear.gif"# Store the file name of your shape(s)
new_letter = ''

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) 
wn.addshape(pear_image)# Make the screen aware of the new file

apple = trtl.Turtle()
pear = trtl.Turtle()
apple.penup()
pear.penup()
drawer = trtl.Turtle()
drawer.penup()

letters = ['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_a_letter()
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def falling_apple():
  drawer.clear()
  wn.tracer(True)
  x = apple.xcor()
  y = apple.ycor()
  while (y > -150):
    apple.goto(x,y)
    y -= 2
  apple.hideturtle()

# This function takes care of font and color.
def draw_a_letter():
  global new_letter
  wn.tracer(False)
  drawer.color("white")
  drawer.goto(apple.xcor()-19,apple.ycor()-40)
  new_letter = rand.choice(letters)
  letters.remove(new_letter)
  drawer.write(new_letter, font=("Arial", 40, "bold"))


#-----function calls-----
draw_apple(apple)

#draw_pear(pear)
#falling_apple()

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

#for i in range(0, number_of_apples):
  
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.




# This call to the onkeypress function sets falling_apple as the function
# that will be called when the "new letter" key is pressed.
wn.onkeypress(falling_apple, new_letter)

#wn.update()
wn.listen()

wn.mainloop()