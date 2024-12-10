def data_loader(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        reports = [line.split(' ') for line in lines]
    return reports

def process_report_part1(report):
    diff = [int(j) - int(i) for i, j in zip(report, report[1:])]
    # Check conditions
    if (all(value > 0 for value in diff) or all(value < 0 for value in diff)):
        if max([abs(value) for value in diff]) <=3:
            if min([abs(value) for value in diff])>=1:
                return True
    return False
    
def process_report_part2(report):
    for i in range(len(report)):
        list1 = report[:i]
        list2 = report[i+1:]
        task_removed_list = list1 + list2
        processed_report = process_report_part1(task_removed_list)
        if processed_report:
            return True

def process_all_reports(reports, part='1'):
    processed_reports = [process_report_part1(report) for report in reports] if part == '1' else [process_report_part2(report) for report in reports]
    return processed_reports.count(True)


if __name__ == '__main__':
    reports = data_loader('input')
    safe_reports = process_all_reports(reports)
    print('Number of safe reports meeting criteria (part 1): ', safe_reports)
    safe_reports2 = process_all_reports(reports=reports, part='2')
    print('Number of safe reports meeting criteria (part 2): ', safe_reports2)
