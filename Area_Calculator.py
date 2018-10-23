'''This program is used to calculate the area of triangle and circle using python
'''
print 'Calculator is Loading. . . .'
#Option to select the area
option = raw_input("Enter C for Circle or T for Triangle: ")
# For calculating area of circle
if option == 'C':
  radius = float(raw_input("Enter the radius of circle: "))
  area = 3.14159 * radius ** 2
  print "The area of circle is %f." % (area)
# For calculating area of triangle
elif option == 'T':
  base = float(raw_input("Enter the base of triangle: "))
  height = float(raw_input("Enter the height of triangle: "))
  area = 0.5 * base * height
  print "The area of triangle is %f." % (area)
# If input given is invalid
else:
  print "Sorry! you entered a invalid shape"
#End of the program!