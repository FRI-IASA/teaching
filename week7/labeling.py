import os
import glob
import cv2
import numpy as np

folders = [name for name in os.listdir(".") if os.path.isdir(name)]
print (folders)

num_classes = len(folders)
data_dictionary= {}

for i in range(num_classes):
	data_dictionary[folders[i]] = sorted(glob.glob('./'+folders[i]+'/*.jpg'))

print (data_dictionary)
# Creating a numpy array to get 3 images, each has a 4096 * 3072* 3 dimensions
all_data = np.zeros((3,4096,3072,3))
all_labels = np.zeros((3,num_classes))   #dog = [1,0], #cat = [0,1]
counter=0
for i, folder_name in enumerate(folders):
	for j in range(len(data_dictionary[folder_name])):

		img = cv2.imread(data_dictionary[folder_name][j])
		#img = cv2.imread('cat.jpg',0)   #This converts the image to grayscale
		print (folder_name)
		print ('\nimg name is ',data_dictionary[folder_name][j])


		print ('\nimg shape is:')
		print (img.shape)

		# Converting BGR to RGB because cv2 works in BGR
		# While matplotlib works in RGB
		img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		print (i*len(data_dictionary[folder_name])+j)
		all_data[counter,:,:,:] = img
		if folder_name =='dog':
			all_labels[counter,:] =np.array([1,0])
		else:
			all_labels[counter,:] =np.array([0,1])

		counter+=1

print (all_labels[:,:])