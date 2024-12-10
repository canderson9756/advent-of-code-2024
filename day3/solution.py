import re

def data_loader(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def find_multiplications(lines):
    expression = "mul\([0-9]*,[0-9]*\)"
    multiplication_sequence = []
    for line in lines:
        multiplication_sequence.extend(re.findall(expression, line))
    return multiplication_sequence
    
def find_multiplications_do_dont(lines):
    expression = "mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)"
    multiplication_sequence = []
    for line in lines:
        multiplication_sequence.extend(re.findall(expression, line))
    return multiplication_sequence

def calculate_total_do_dont(multiplication_sequence):
    do_dont_flag = True
    total = 0
    for multiplication in multiplication_sequence:
        if do_dont_flag and 'mul' in multiplication:
            (a, b) = multiplication.strip('mul()').split(',')
            total += int(a) * int(b)
        elif "don't" in multiplication:
            do_dont_flag = False
        elif "do" in multiplication:
            do_dont_flag = True
    return total    

def calculate_total(multiplication_sequence):
    total = 0
    for multiplication in multiplication_sequence:
        (a, b) = multiplication.strip('mul()').split(',')
        total += int(a) * int(b)
    return total

if __name__ == '__main__':
    lines = data_loader('input')
    multiplication_sequence = find_multiplications(lines)
    multiplication_total = calculate_total(multiplication_sequence)
    print('Total of correct multiplications (part 1): ', multiplication_total)
    multiplication_sequence = find_multiplications_do_dont(lines)
    multiplication_total = calculate_total_do_dont(multiplication_sequence)
    print('Total of correct multiplications (part 2): ', multiplication_total)