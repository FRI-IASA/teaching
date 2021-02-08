# Sys is used to exit the program in case the libraries needed are not isntalled
import sys

try:
    import cv2
except:
    print("You need to install Opencv \n Run this command \n pip install python-opencv")
    sys.exit(1)
#Numpy will be installed along Open-cv automatically
import numpy as np

try:
	# We use matplotlib to display and image
    from matplotlib import pyplot as plt
except:
    print("You need to install matplotlib \n Run this command \n pip install matplotlib")
    sys.exit(1)

# Loading cat.jpg or replace it with another custom image
img = cv2.imread('cat.jpg')
#img = cv2.imread('cat.jpg',0)   #This converts the image to grayscale

print ('\nimg is in the form of:',type(img))


print ('\nimg shape is:')
print (img.shape)

# Converting BGR to RGB because cv2 works in BGR
# While matplotlib works in RGB
img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
