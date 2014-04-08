# Anthony Lim
# alim4@ucsc.edu
#
# CMPS 5P, Spring 2014
# Assignment 1
#
# A simple program to calculate the area of a circle

__author__ = 'anthonylim'

import math

# These are intended for global use
length1 = 0
length2 = 0
length3 = 0

# Prompts the user for number input to use for triangle calculations
def prompt_user():
    global length1, length2, length3
    while True:
        try:
            length1 = float(raw_input('Please input a number for side 1 of a triangle: '))
            length2 = float(raw_input('Please input a number for side 2 of a triangle: '))
            length3 = float(raw_input('Please input a number for side 3 of a triangle: '))
            break
        except ValueError:
            print("That's not a valid number. Please try again.")


#def sanity_check():



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
    """
    :param l1: length 1 for triangle
    :param l2: length 2 for triangle
    :param l3: length 3 for triangle
    :return: the area of the triangle using Heron's formula
    """
    s = (0.5) * (l1 + l2 + l3)  # Half of the perimeter
    area = math.sqrt(s * ((s - l1) * (s - l2) * (s - l3)))
    return area


def calculate_angle(l1, l2, area):
    """
    :param l1: side length
    :param l2: base length
    :param area: area of the triangle
    :return: the angle between the two sides, in radians
    """
    angle = math.asin((2 * area) / (l1 * l2))
    return angle


# Init
prompt_user()

# Function calls to get numbers from user input
perimeter = calculate_perimeter(length1, length2, length3)
area = calculate_area(length1, length2, length3)
angle1 = math.degrees(calculate_angle(length1, length2, area))
angle2 = math.degrees(calculate_angle(length2, length3, area))
angle3 = math.degrees(calculate_angle(length3, length1, area))

# Result
print('Given the triangle sides of {0}, {1}, and {2}...'.format(length1, length2, length3))
print('The perimeter of the triangle is {0} and the area is {1:.2f}'
      .format(perimeter, area))
print('The three angles are {0:.2f}, {1:.2f}, and {2:.2f}'.format(angle1, angle2, angle3))
