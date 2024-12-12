def data_loader(filename='input'):
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [d.strip() for d in data]
    return data

def check_next_letter(wordsearch, x_start, y_start, x_inc, y_inc, word='XMAS'):
    word = word[1:]
    if not word:
        return 1
    x_new, y_new = x_start + x_inc, y_start +y_inc
    if x_new == len(wordsearch[0]) or x_new < 0 or y_new == len(wordsearch) or y_new < 0:
        return 0
    next_letter = wordsearch[y_start +y_inc][x_start + x_inc]
    if next_letter == word[0]:
        return check_next_letter(wordsearch, x_new, y_new, x_inc, y_inc, word=word)
    else:
        return 0
    return 0

def check_puzzle_2_case1(wordsearch, j, i):
    indices_to_check = {(i, j+2): 'S',
                        (i+1, j+1): 'A',
                        (i+2, j): 'M',
                        (i+2, j+2): 'S'
                        }  
    for key, value in indices_to_check.items():
        if key[0] >= len(wordsearch) or key[0] < 0  or key[1] >= len(wordsearch[0]) or key[0] < 0:
            return 0
        elif wordsearch[key[0]][key[1]] == value:
            continue
        else:
            return 0
    return 1

def check_puzzle_2_case2(wordsearch, j, i):
    indices_to_check = {(i, j+2): 'M',
                        (i+1, j+1): 'A',
                        (i+2, j): 'S',
                        (i+2, j+2): 'S'
                        }  
    for key, value in indices_to_check.items():
        if key[0] >= len(wordsearch) or key[0] < 0  or key[1] >= len(wordsearch[0]) or key[0] < 0:
            return 0
        elif wordsearch[key[0]][key[1]] == value:
            continue
        else:
            return 0
    return 1


def check_puzzle_2_case3(wordsearch, j, i):
    indices_to_check = {(i, j+2): 'S',
                        (i+1, j+1): 'A',
                        (i+2, j): 'M',
                        (i+2, j+2): 'M'
                        }  
    for key, value in indices_to_check.items():
        if key[0] >= len(wordsearch) or key[0] < 0  or key[1] >= len(wordsearch[0]) or key[0] < 0:
            return 0
        elif wordsearch[key[0]][key[1]] == value:
            continue
        else:
            return 0
    return 1

def check_puzzle_2_case4(wordsearch, j, i):
    indices_to_check = {(i, j+2): 'M',
                        (i+1, j+1): 'A',
                        (i+2, j): 'S',
                        (i+2, j+2): 'M'
                        }  
    for key, value in indices_to_check.items():
        if key[0] >= len(wordsearch) or key[0] < 0  or key[1] >= len(wordsearch[0]) or key[0] < 0:
            return 0
        elif wordsearch[key[0]][key[1]] == value:
            continue
        else:
            return 0
    return 1

def parse_wordsearch(wordsearch, word='XMAS'):
    word_count_part1 = 0
    word_count_part2 = 0
    for i, row in enumerate(wordsearch):
        for j, letter in enumerate(row):
            if letter == 'X':
                word_count_part1 += check_next_letter(wordsearch, j, i, 1, 0, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, 1, 1, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, 0, 1, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, -1, 0, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, -1, -1, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, 0, -1, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, 1, -1, word='XMAS')
                word_count_part1 += check_next_letter(wordsearch, j, i, -1, 1, word='XMAS')
            elif letter == 'M':
                word_count_part2 += check_puzzle_2_case1(wordsearch, j, i)
                word_count_part2 += check_puzzle_2_case2(wordsearch, j, i)
            elif letter == 'S':
                word_count_part2 += check_puzzle_2_case3(wordsearch, j, i)
                word_count_part2 += check_puzzle_2_case4(wordsearch, j, i)
                

    return word_count_part1, word_count_part2

if __name__ == '__main__':
    wordsearch = data_loader('input')
    word_count_part1, word_count_part2 = parse_wordsearch(wordsearch)
    print('Total number of XMAS found: ', word_count_part1)
    print('Total of X-MAS found: ', word_count_part2)