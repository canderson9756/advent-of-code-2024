def data_loader(filename='input'):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def check_next_letter(wordsearch, x_start, y_start, x_inc, y_inc, word='XMAS'):
    word = word[1:]
    if not word:
        return 1
    x_new, y_new = x_start + x_inc, y_start +y_inc
    print(x_new, y_new)
    if x_new == len(wordsearch[0]) or x_new < 0 or y_new == len(wordsearch) or y_new < 0:
        return 0
    next_letter = wordsearch[x_start + x_inc][y_start +y_inc]
    if next_letter == word[0]:
        check_next_letter(wordsearch, x_new, y_new, x_inc, y_inc, word=word)
    else:
        return 0
    return 0

def parse_wordsearch(wordsearch, word='XMAS'):
    word_count = 0
    for i, row in enumerate(wordsearch):
        for j, letter in enumerate(row):
            if letter == 'X':
                word_count += check_next_letter(wordsearch, j, i, 1, 0, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, 1, 1, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, 0, 1, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, -1, 0, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, -1, -1, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, 0, -1, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, 1, -1, word='XMAS')
                word_count += check_next_letter(wordsearch, j, i, -1, 1, word='XMAS')
    return word_count

if __name__ == '__main__':
    wordsearch = data_loader()
    word_count = parse_wordsearch(wordsearch)
    print('Total number of XMAS found: ', word_count)