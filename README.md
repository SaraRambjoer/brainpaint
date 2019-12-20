# brainpaint
Image creation library using the brainfrick programming language

The brainfrick programming language, perhaps more known by the more vulgar brainf\*\*k, is an esoteric programming language originally created to create a programming language with a small compiler (For more history see https://esolangs.org/wiki/Brainfuck). 

The programming language works by moving a memory pointer around a one-dimensional memory consisting of distinct memory cells. The language
can increment, decrement, output memory contents or write in user input, and can check the memory contents for flow control. 

This library contains an interpreter for brainfrick written in python, as well as a program for creating images based on the memory contents in
the brainfrick abstract machine after the program has finished executing. The program creates square images and if the amount of included
memory cells is not a square of a whole number the program pads at the end with transparent pixels. Three memory cells in the brainfrick "VM" equates to one pixel, going in the order RGB. 

Also included is a brainfrick program that can create images by writing the values of each pixel. 
