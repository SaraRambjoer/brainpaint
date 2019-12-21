# brainpaint
Image creation library using the brainfrick programming language

The brainfrick programming language, perhaps more known by the more vulgar brainf\*\*k, is an esoteric programming language originally created to create a programming language with a small compiler (For more history see https://esolangs.org/wiki/Brainfuck). 

The programming language works by moving a memory pointer around a one-dimensional memory consisting of distinct memory cells. The language
can increment, decrement, output memory contents or write in user input, and can check the memory contents for flow control. 

This library contains an interpreter for brainfrick written in python, as well as a program for creating images based on the memory contents in
the brainfrick abstract machine after the program has finished executing. The user specifies image size when calling the createimage.py script. Three memory cells in the brainfrick "VM" equates to one pixel, going in the order RGB. Defaults to value 0 in each color band as that is the default value in bf memory cells. 

Also included is a brainfrick program that can create images by writing the values of each pixel (pixel_by_pixel.txt)

createimage.py
--output_path : The filename including the path of the new image you want to create
--input_path  : The filename including the path of the brainfrick code you want to execute
--xdim        : How many pixels there should be in the x-dimension in the output image
--ydim        : How many pixels there should be in the y-dimension in the output image.
