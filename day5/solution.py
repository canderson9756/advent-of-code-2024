def rule_loader(filename='input_rules'):
    with open(filename, 'r') as f:
        rules = f.readlines()
    rules = [rule.strip().split('|') for rule in rules]
    rules_dict = {}
    for rule in rules:
        if rule[0] not in rules_dict:
            rules_dict[rule[0]] = [rule[1]]
        else:
            rules_dict[rule[0]].append(rules[1])
    return rules_dict

def data_loader(filename='input'):
    with open(filename, 'r') as f:
        data = f.readlines()
    data = [pages.strip().split(',') for pages in data]
    return data

def process_update(update, rules):
    for page in update:
        page_index = update.index(page)
        rule_values = rules[page]
        if page_index < rule_index:
            continue
        else:
            return False
    return True

def process_all_updates(updates, rules):
    total = 0
    for update in updates:
        processed_update = process_update(update, rules)
        if processed_update:
            total += int(update[int((len(update)/2))])
    return total

if __name__ == '__main__':
    rules = rule_loader()
    data = data_loader()
    total_part1 = process_all_updates(data, rules)
    print('Total is: ', total_part1)
