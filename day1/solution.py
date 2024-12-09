import pandas as pd

def data_loader_pandas(filename, delimiter=','):
    data = pd.read_csv(filename, delimiter=delimiter, header=None)
    list1, list2 = data.iloc[:, 0].tolist(), data.iloc[:,1].tolist()
    return list1, list2

def data_loader_text(filename, delimiter='   '):
    list1, list2 = list(), list()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data_values = line.split(delimiter)
            list1.append(int(data_values[0]))
            list2.append(int(data_values[1]))
    return list1, list2

def process_lists_part1(list1, list2, diff_list=[]):
    list1.sort()
    list2.sort()
    diff_list = [abs(i - j) for (i, j) in zip(list1, list2)]
    return sum(diff_list)

def process_lists_part2(list1, list2):
    similarity_score = 0
    for value in list1:
        similarity_score += list2.count(value) * value
    return similarity_score

if __name__=='__main__':
    list1, list2 = data_loader_text('input', '   ')
    sum_value = process_lists_part1(list1, list2)
    similarity_score = process_lists_part2(list1, list2)

    print("Part one (total distance): ", sum_value)
    print("Part two (similarity score): ", similarity_score)
