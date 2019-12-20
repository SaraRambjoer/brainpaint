"""
Defines supporting functions for binary strings defined as python strings.

This is obviously inefficient as it stores a bit as a character, which can vary in size depending on encoding but is
always greater or equal to one bit. This is nevertheless done for quick development and because my main concern is the
functionality of brainpaint and not the optimality - it is after all a niche use of an esoteric programming language.

"""

def bin_plus(line1, line2):
    """
    :param line1: A binary number of same length as line2
    :param line2: A binary number of same length as line1
    :return: binary sum of line1 and line 2 with underflow
    """
    output = ""
    carry = 0
    for num in range(len(line1) - 1, -1, -1):
        if carry == 0:
            if line1[num] != "0" and line2[num] != "0":
                output = "0" + output
            elif line1[num] == "1" and line2[num] == "1":
                carry = 1
                output = "0" + output
            else:
                output = "1" + output
        else:
            carry = 0
            if line1[num] != "0" and line2[num] != "0":
                output = "1" + output
            elif line1[num] == "1" and line2[num] == "1":
                carry = 1
                output = "1" + output
            else:
                carry = 1
                output = "0" + output
    return output


def twos_complement(bin_num):
    """
    :param bin_num: A binary number
    :return: Twos complement of bin_num
    """
    output = ""
    for bit in bin_num:
        if bit == "0":
            output += "1"
        else:
            output += "0"
    return bin_plus(output, "0" * (len(bin_num) -1) + "1")  # output + 1


def bin_minus(term1, term2):
    """
    :param term1: s.t. result is term1 - term2
    :param term2: s.t. result is term1 - term2
    :result: term1 - term2
    """
    return bin_plus(term1, twos_complement(term2))

def make_integer(bin_num):
    """
    :param bin_num: A binary number represented as a string
    :return: Returns a base 10 representation of the number, using python ints.
    """
    output = 0
    negative = bin_num[0] == "1"
    if negative:
        bin_num = twos_complement(bin_num) # Twos complement of negative number is positive number

    for num in range(len(bin_num)-1, -1, -1):
        output += int(bin_num[num]) * pow(2, len(bin_num)-1-num)

    if negative:
        return -1 * output
    else:
        return output

def map_to(original_range, new_range):
    """
    :param original_range: An integer representing difference between minimal and maximal value in an continous
        integer domain
    :param new_range: An integer representing difference between minimal and maximal value in an continous
        integer domain
    :return: a function giving a linear mapping between the domains
    """
    if original_range == 0:
        return lambda x: new_range  # if new_range is 0 just map anything to max value in orginal
    return lambda x: x * new_range/original_range