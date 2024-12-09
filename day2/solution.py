def data_loader(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        reports = [line.split(' ') for line in lines]
    return reports

def process_report(report):
    diff = [int(j) - int(i) for i, j in zip(report, report[1:])]
    # Check conditions
    if (all(value > 0 for value in diff) or all(value < 0 for value in diff)):
        if max([abs(value) for value in diff]) <=3:
            if min([abs(value) for value in diff])>=1:
                return True
    return False
    
def process_all_reports(reports):
    processed_reports = [process_report(report) for report in reports]
    return processed_reports.count(True)


if __name__ == '__main__':
    reports = data_loader('input')
    safe_reports = process_all_reports(reports)
    print('Number of safe reports meeting criteria: ', safe_reports)