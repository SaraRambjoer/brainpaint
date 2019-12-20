import binary_support

"""
Implementation of the Brainfrick (also known as the more vulgar Brainf**k) language. Implementation assumes the program
does not attempt to point to negative addresses.
"""

class Brainfrick():
    def __init__(self, tape_size, cell_size):
        """
        :param tape_size: designate amount of cells in memory
        :param cell_size: designate amount of bits per cell
        """
        self.tape_size = tape_size
        self.cell_size = cell_size
        self.memory = ["0" * cell_size] * tape_size
        self.memory_pointer = 0
        self.instruction_pointer = 0
        self.one = "0" * (self.cell_size - 1) + "1"
        self.zero = "0" * self.cell_size
        self.program = None

    def move_pointer_right(self):
        if self.memory_pointer + 1 < self.tape_size:
            self.memory_pointer += 1
        self.instruction_pointer += 1

    def move_pointer_left(self):
        if self.memory_pointer - 1 < 0:
            self.memory_pointer -= 1
        self.instruction_pointer += 1

    def increment(self):
        binary_support.bin_plus(self.memory[self.memory_pointer], self.one)
        self.instruction_pointer += 1

    def decrement(self):
        binary_support.bin_minus(self.memory[self.memory_pointer], self.one)
        self.instruction_pointer += 1

    def print_cell(self):
        self.instruction_pointer += 1

    def input_cell(self):
        the_input = str(input("Input cell value as binary string: "))
        for char in the_input:
            if char != "0" and char != "1":
                raise ValueError("Input value must only consist of 0 and 1s.")
        if len(the_input) < self.cell_size:
            the_input = "0" * (self.cell_size - len(the_input)) + the_input  # Pad input with 0 if too short
        elif len(the_input) > self.cell_size:
            raise ValueError("Input value too large.")
        self.memory[self.memory_pointer] = the_input
        self.instruction_pointer += 1

    def jump_forward(self):
        if self.memory[self.memory_pointer] == self.zero:
            found_opens = 0
            self.instruction_pointer += 1
            # An index error occuring here means the program has no ']' matching the opening '['.
            while found_opens == 0 and self.program[self.instruction_pointer] != "]":
                if self.program[self.instruction_pointer] == "[":
                    found_opens += 1
                elif self.program[self.instruction_pointer] == "]":
                    found_opens -= 1
                self.instruction_pointer += 1
            self.instruction_pointer += 1
        else:
            self.instruction_pointer += 1

    def jump_backward(self):
        if self.memory[self.memory_pointer] != self.zero:
            found_closeds = 0
            # An index error occuring here means the program has no ']' matching the opening '['.
            while found_closeds == 0 and self.program[self.instruction_pointer] != "[":
                if self.program[self.instruction_pointer] == "]":
                    found_closeds += 1
                elif self.program[self.instruction_pointer] == "[":
                    found_closeds -= 1
                self.instruction_pointer -= 1
            self.instruction_pointer -= 1
        else:
            self.instruction_pointer += 1

    def insert_program(self, program_code):
        """
        :param program_code: A string representing the program code.
        Loads bf program, using the convention that any character not in legal_characters is a comment.
        """
        parsed_code = ""
        legal_characters = ['>', '<', '+', '-', '.', ',', '[', ']']
        for char in program_code:
            if char in legal_characters:
               parsed_code += char
        self.program = parsed_code

    def execute_instruction(self):
        operator = self.program[self.instruction_pointer]
        if operator == '<':
            self.move_pointer_left()
        elif operator == '>':
            self.move_pointer_right()
        elif operator == '+':
            self.increment()
        elif operator == '-':
            self.decrement()
        elif operator == '.':
            self.print_cell()
        elif operator == ',':
            self.input_cell()
        elif operator == '[':
            self.jump_forward()
        elif operator == ']':
            self.jump_backward()

    def run(self):
        while self.instruction_pointer < len(self.program):
            self.execute_instruction()

        # On the end of program write a special EOF-symbol. In bf it is a manner of contention whether one should write
        # -1 to designate having finished program execution or nothing at all. In this implementation we write the
        # string "EOF" at the memory address pointed to by the memory pointer because this is convenient for brainpaint.
        self.memory[self.memory_pointer] = "EOF"



