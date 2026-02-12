'''
author: Lorenzo Manuel
date: February 12, 2026

'''
# Input
import math

radius_c = input("Please enter a number to represent the radius of a circle: ")
length_r = input("Please enter a number that represents the length of a rectangle: ")
width_r = input("Please enter a number that represents the width of a rectangle: ")
sidel_o = input("Please enter a number that represents the side length of an octogon: ")

area_c = math.pi * int(radius_c)**2
perimeter_c = math.pi * int(radius_c) * 2
area_r = int(length_r) * int(width_r)
perimeter_r = (int(length_r) + int(width_r)) * 2
area_o = 2 * int(sidel_o)**2 * (1 + math.sqrt(2))
perimeter_o = int(sidel_o) * 8 

# Processing

# Output
print(f"The circle has an area of {area_c} and a perimeter of {perimeter_c}")
print(f"The rectangle has an area of {area_r} and a perimeter of {perimeter_r}")
print(f"The octagon has an area of {area_o} and a perimeter of {perimeter_o}")
