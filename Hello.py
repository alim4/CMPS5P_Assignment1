# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 1
#
# A simple program to calculate the area of a circle

__author__ = 'anthonylim'

# These are intended for global use
length1 = 0
length2 = 0
length3 = 0

# Prompts the user for number input to use for triangle calculations
def prompt_user():
    global length1, length2, length3
    length1 = float(raw_input('Please input a number for side 1 of a triangle: '))
    length2 = float(raw_input('Please input a number for side 2 of a triangle: '))
    length3 = float(raw_input('Please input a number for side 3 of a triangle: '))



def calculate_perimeter(l1, l2, l3):
    """
    :param l1: length 1 for triangle
    :param l2: length 2 for triangle
    :param l3: length 3 for triangle
    :return: return the calculated perimeter of the triangle
    """
    perimeter = l1 + l2 + l3
    return perimeter

def calculate_area(l1, l2, l3):
    area = 0.5 * 5

prompt_user()

print(length1, length2, length3)
