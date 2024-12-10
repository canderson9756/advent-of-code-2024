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
    print('Total of correct multiplications: ', multiplication_total)