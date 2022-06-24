from tkinter import image_names
import cv2

#Get the image location and image file name
img_location = 'C:/Users/HUNG\Desktop/'
filename = 'images.jpg'

#Read the image
img = cv2.imread(img_location+filename)
#Convert the image to the gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Inverte the image
inverted_gray_image = 255 - gray_image
#Blur the image by gaussian function
blurred_img= cv2.GaussianBlur(inverted_gray_image,(21,21),0)
#Inverted the blurred image
inverted_blurred_img = 255 - blurred_img
#Create the pencil sketch image
pencil_sketch_IMG = cv2.divide(gray_image,inverted_blurred_img,scale=450) 

#Show the image
cv2.imshow('Original Image',img)
cv2.imshow('New image',pencil_sketch_IMG)
cv2.waitKey(0)





