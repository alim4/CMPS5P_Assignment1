CMPS5P_Assignment1
==================

Assignment 1: Fun with Triangles

Description

For this assignment you will write a program to calculate the perimeter of a triangle, area of a triangle, and interior angles in the triangle given the lengths of its three sides. This will require writing three functions:

Calculate perimeter given the three sides
Calculate area given the three sides
Calculate one angle given three sides.  The angle should be the one opposite the first side (of the three parameters you're passing to the function).  You'll need to call this function three times.
Your program should prompt the user to enter three numbers representing the length of each side of the triangle, and then pass these numbers as the parameters to each function. All three functions should return a result and that result should be printed.  As noted above, you'll need to call one function three times to get three answers.  Your angles should be printed in  degrees—since Python uses radians, for its trig functions, you might need to convert from radians to degrees before printing. 

Requirements

Use the raw_input() function to read in three values from a user. Each value will represent the length of one side of the triangle. You'll need to call raw_input() three times to do this. You'll also need to call float() to convert the input into a floating-point number.
Write three distinct functions, one to calculate the area of the triangle, one to calculate the angle opposite the first side passed, and one for the perimeter. Each function should take the three values read from the user as arguments, one for each of the sides.
Call the function that calculates angles three times, once for each angle. Obviously, it doesn't matter which order the second and third side are specified in, but the first side should determine the angle you're calculating.
Sample output
Your output should look something like this. We're not going to be exact on this assignment, as long as you have the basic information your program should print out (this may change in future assignments, though).

For a triangle with sides 3.0, 4.0, 5.0, area is 6.0 and perimeter is 12.0.
The three angles are 36.87, 53.13, 90.00.
General Requirements

These requirements apply to all programming assignments.

Your program must contain a comment at the top with your name, UCSC gold ID (your ucsc.edu email address), and the assignment number.
Your program must not contain any syntax errors! Any program with syntax errors will receive a maximum grade of 5 points. If Python can't interpret the program you wrote, we won't try to grade it. We will grade a program with other types of errors (runtime, semantic), though such a program will (obviously) receive a lower grade than a program that works correctly.
Document your sources! For example, any formula used to calculate the area of a triangle must be cited (unless of course you just knew it). You can document this with a simple comment in your program.
Use source code control (git is well-integrated with PyCharm) to track your progress in writing your code.  You must turn in your commit log as well as your program.  Your commit log should show your progress in getting your program written.
Hints

What to Turn In

You should submit a single file for this assignment: the plain text file that contains your program. The file must have a name that ends in .py; for example, you could call your program assignment1.py or triangle.py.

Example Program

This is a simple example of the type of program we'd like to see from you. Note the comment at the top with the UCSC gold ID and the citation of sources above the formula for calculating the area of the circle.

# Ethan Miller
# elm@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 1
#
# A simple program to calculate the area of a circle

__author__ = 'elm'

# This formula for the area of a circle was taken from
# http://mathworld.wolfram.com/Circle.html
#
# The value of pi was obtained from Wikipedia:
# http://en.wikipedia.org/wiki/Pi
def circle_area (radius):
    '''
    Calculates the area of a circle given the radius.
    '''
    pi = 3.1415926535897932
    area = pi * (radius ** 2)
    return (area)

radius = float (raw_input ('What is the length of the radius? '))
area = circle_area (radius)
print ('The area of the circle with radius {0} is {1}'.format(radius, area))
Hints

Start early!
Think about what your program needs to do before starting to write Python code.
Go to lab sections this week (Tue
Don't panic! If you're having trouble, attend lab sections or visit office hours! We're here to help!
Some things are OK to look up online...
Not knowing how to calculate the area of a triangle given only three sides is OK; Google it. The important part here is not the math, but the program. If you do look up a formula, be sure to cite the source!.
Find a formula that only uses the sides (and optionally the perimeter) of the triangle. You shouldn't use formulæ that require the use of trig functions like sine and cosine.
You may have to use square roots to solve this problem; remember that √x = x1/2.
You also might not know how to calculate the angles of a triangle.  Again, you're encouraged to use a search engine and/or read a trig textbook to find the answer.  However, you may  not ask someone else directly for the formula.  Part of the goal of this assignment is for you to learn how to find answers to problems and incorporate them into your code.
Remember that functions can call other functions.
You might want to use trigonometric functions, which you can get from the math library.  For example, if you wanted access to the sin function, you could get it by including this line in your program:
from math import sin
If you wanted both sine and arcsine (inverse sine), you could do:

from math import sin, asin
Note that Python uses the abbreviation sin for sine; it does the same for other trig functions. The inverse functions are preceded by an a (for arc). Also, Python, like many other programming languages, does its angle calculations in radians, by default, so you'll want to convert them to degrees.
