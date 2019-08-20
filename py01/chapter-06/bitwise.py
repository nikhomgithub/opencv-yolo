# USAGE
# python bitwise.py

# Import the necessary packages
import numpy as np
import cv2

#a=np.zeros(270000)
#a=a.reshape((300,300,3))
a=np.zeros((300,300,3), dtype = "uint8")
a[0:100, 0:100] = (0, 255, 0)
cv2.imshow("a",a)

corner = a[0:100, 0:100]
cv2.imshow("corner",corner)

# First, let's draw a rectangle
rectangle = np.zeros((300, 300,1), dtype = "uint8")
#print(rectangle.shape)
cv2.rectangle(rectangle, (25, 25), (275, 275), 200, -1)
cv2.imshow("Rectangle", rectangle)

# Secondly, let's draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150),150,200,-1)
cv2.imshow("Circle", circle)

# A bitwise 'AND' is only True when both rectangle
# and circle have a value that is 'ON'. Simply put,
# the bitwise_and function examines every pixel in
# rectangle and circle. If both pixels have a value
# greater than zero, that pixel is turned 'ON' (i.e
# set to 255 in the output image). If both pixels
# are not greater than zero, then the output pixel
# is left 'OFF' with a value of 0.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)


# A bitwise 'OR' examines every pixel in rectangle
# and circle. If EITHER pixel in rectangle or circle
# is greater than zero, then the output pixel has a
# value of 255, otherwise it is 0.
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)


# The bitwise 'XOR' is identical to the 'OR' function,
# with one exception: both rectangle and circle are
# not allowed to have values greater than 0.
# XOR=OR-AND
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)


# Finally, the bitwise 'NOT' inverts the values of
# the pixels. Pixels with a value of 255 become 0,
# and pixels with a value of 0 become 255.
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
print(circle[150,150])


cv2.waitKey(10000)