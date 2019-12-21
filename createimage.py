import brainfrick
import argparse
import binary_support
from PIL import Image
import math

"""
Works by reading off 3 cell values for each pixel going in order rgb from the memory contents of the brainfrick VM
after finishing execution of loaded program. 
"""

parse = argparse.ArgumentParser(description="Input paramaters for brainpaint")
parse.add_argument("--input_path", help="Path to brainfrick code")
parse.add_argument("--output_path", help="Path where output should be saved")
parse.add_argument("--xdim", help="Specifies the x-dimension of the output image")
parse.add_argument("--ydim", help="Specifies the y-dimension of the output image")

args = vars(parse.parse_args())
code_file = open(args["input_path"], 'r')
program = code_file.read()
code_file.close()

bf = brainfrick.Brainfrick(30000, 9)  # using 9 bit cells as a values for rgb are given between 0 and 255, and the msb
# is used for negative and positive numbers (negative numbers don't make sense for images but it does make sense to
# support them in the other functions)

bf.insert_program(program)
bf.run()
memory = bf.memory
dim1, dim2 = int(args["xdim"]), int(args["ydim"])

last_index = dim1*dim2*3
memory = memory[:last_index]
new_memory = []
# make every number positive
for bin_num in memory:
    num = binary_support.make_integer(bin_num)
    if num < 0:
        num = -num
    new_memory.append(num)


# map every number to a value between 0 and 255, use this if changing bits per cell
# map256 = binary_support.map_to(max(new_memory)-min(new_memory), 256)
# memory_map256 = map(map256, new_memory)


# deprecated in favour of user specified image dimensions
def approximate_dimensions(size):
    size = size/3  # because there are 3 cells per pixel
    square = math.sqrt(size)
    return int(math.ceil(square)), int(math.ceil(square))



image = Image.new("RGBA", (dim1, dim2))
for num1 in range(dim2):
    # for each row
    for num2 in range(dim1):
        # for each column
        cellsInPreviousRows = num1*dim1  # amount of rows visited * length of row
        nextRed = (cellsInPreviousRows+num2)*3  # pixels in previous rows + visited pixels in this row + 1 (+1 implicit
        # this being next iteration) gives next
        # times three since there are three memory cells per pixel
        val1, val2, val3 = new_memory[nextRed], new_memory[nextRed+1], new_memory[nextRed+2]  # Going in order RGB
        print(num2, num1)
        image.putpixel((num2, num1), (val1, val2, val3, 255))  # (num2, num1) since num1 is y and num2 is x


image.save(args["output_path"])
image.close()

