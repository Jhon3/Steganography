
# Steganography

A program that hides a message in a image with bitmap  (bmp) format and another program that reveals the hidden message. For the implementation of the programs, the OpenCV computer vision library was used.
Before running the code you need to install the following libraries using the commands with python 3:

OpenCV
> pip3 install opencv-python

Numpy
>pip3 install numpy

## Execute

To hide a particular message in an image you need to execute the file *hide.py* as follows:
> python3 hide.py msg.txt wolf.bmp 

Note that in the execution of the python script was passed the txt file (msg.txt )containing the message you want to hide and the image (wolf.bmp) that will receive the message. The image with the hidden message will be saved in the **imageResult** folder.
To reveal the message hidden in the image just run the file *revel.py* as follows:
> python3 revel.py ./imageResult/wolf.bmp 

This time it was only necessary to insert the image with message is hidden. The message will be printed on the screen and it will be saved to a txt file in the **textResult** folder.
