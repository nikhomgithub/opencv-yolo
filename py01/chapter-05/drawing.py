# USAGE
# python drawing.py

# Import the necessary packages
import numpy as np
import cv2

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

#smallcanvas = canvas[0:100,0:100]
#cv2.imshow("Small Canvas",smallcanvas)

# Draw a green line from the top-left corner of our canvas
# to the bottom-right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (50, 300), green)
cv2.imshow("Canvas", canvas)

#cv2.waitKey(9000)

# Now, draw a 3 pixel thick red line from the top-right
# corner to the bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
#cv2.waitKey(9000)

# Draw a green 50x50 pixel square, starting at 10x10 and
# ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
#cv2.waitKey(9000)

# Draw another rectangle, this time we'll make it red and
# 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
#cv2.waitKey(9000)

# Let's draw one last rectangle: blue and filled in
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
#cv2.waitKey(9000)

# Reset our canvas and draw a white circle at the center
# of the canvas with increasing radii - from 25 pixels to
# 150 pixels
canvas2 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas2.shape[1]//2, canvas2.shape[0]//2)
print("Center=")
print(centerX)#150
print(centerY)#150
white = (255, 255, 255)

for r in range(0, 175, 25):
	cv2.circle(canvas2, (centerX, centerY), r, white)

cv2.imshow("Canvas2", canvas2)


# Let's go crazy and draw 25 random circles
for i in range(0, 25):
	# randomly generate a radius size between 5 and 200,
	# generate a random color, and then pick a random
	# point on our canvas where the circle will be drawn
	radius = np.random.randint(5, high = 200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	pt = np.random.randint(0, high = 300, size = (2,)).tolist()
	# draw our random circle
	cv2.circle(canvas2, tuple(pt), radius, color)
	cv2.imshow("Canvas2", canvas2)
print(radius)
print(color)
print(pt)


# Show our masterpiece

cv2.waitKey(7000)