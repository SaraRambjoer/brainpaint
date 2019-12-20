import brainfrick
import argparse
import binary_support
from PIL import Image
import math

"""
Works by reading off 3 cell values for each pixel going in order rgb
"""

parse = argparse.ArgumentParser(description="Input paramaters for brainpaint")
parse.add_argument('--input_path', help='Path to brainfrick code')
parse.add_argument('--output_path', help='Path where output should be saved')

args = vars(parse.parse_args())
code_file = open(args["input_path"], 'r')
program = code_file.read()
code_file.close()

bf = brainfrick.Brainfrick(30000, 8)  # using 8 bit cells as a values for rgb are given between 0 and 255
bf.insert_program(program)
bf.run()
memory = bf.memory


last_index = memory.index("EOF")
memory = memory[0:last_index]

new_memory = []
# make every number positive
for bin_num in memory:
    num = binary_support.make_integer(bin_num)
    if num < 0:
        num = - num
    new_memory.append(num)


# map every number to a value between 0 and 255, use this if changing bits per cell
# map256 = binary_support.map_to(max(new_memory)-min(new_memory), 256)
# memory_map256 = map(map256, new_memory)


def approximate_dimensions(size):
    size = size/3  # because there are 3 cells per pixel
    square = math.sqrt(size)
    return int(math.ceil(square)), int(math.ceil(square))


dim1, dim2 = approximate_dimensions(len(new_memory))

image = Image.new('RGBA', (dim1, dim2))
print(new_memory)
for num in range(dim1):
    for num2 in range(dim2):  # steps of 3 since there are red, green and blue values
        if num*dim2 + num2 < len(new_memory):
            val1, val2, val3 = new_memory[num*dim2 + num2], new_memory[num*dim2 + num2+1], new_memory[num*dim2 + num2+2]
            image.putpixel((num2, num), (val1, val2, val3, 255))


image.save(args["output_path"])
image.close()

