input_file = "day05/input.txt"
sample_file = "day05/sample.txt"


def sum_mid_page_updates(data_file) -> int:
    result = 0
    # data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    data = open(data_file).read().split('\n\n')
    rules = [[int(s) for s in line.split('|')] for line in data[0].splitlines()]
    updates = [[int(s) for s in line.split(',')] for line in data[1].splitlines()]
    print(len(rules))
    print(len(updates))

    for updates_block in updates:
        print('Updates block: {}'.format(updates_block))
        max_index = len(updates_block)-1
        block_index = 0
        rule_broken = False
        for page in updates_block:
            for rule in rules:
                if page == rule[0]:
                    # print("RULEMATCH: This page must be BEFORE {} <- {}".format(page, rule[1]))
                    # Scan if left of us ISN'T the other page number
                    for i in range(block_index):
                        if rule[1] == updates_block[i]:
                            print("RULEBREAK: page [ {} ] isn't BEFORE <- [ {} ]".format(page, rule[1]))
                            rule_broken = True
                            break
                elif page == rule[1]:
                    # print("RULEMATCH: This page must be AFTER  {} -> {}".format(page, rule[0]))
                    # Scan if right of us ISN'T the other page number
                    for i in range(block_index, len(updates_block)-1):
                        if rule[0] == updates_block[i]:
                            print("RULEBREAK: page [ {} ] isn't AFTER  -> [ {} ]".format(page, rule[0]))
                            rule_broken = True
                            break
            block_index+=1
        if not rule_broken:
            result_index = int((len(updates_block)-1)/2)
            print('Valid Update mid: [{}]'.format(updates_block[result_index]))
            result += updates_block[result_index]
    return result

def fix_and_sum_mid_page_updates(data_file) -> int:
    result = 0
    # data = [[int(s) for s in line.split()] for line in open(data_file).read().strip().splitlines()]
    data = open(data_file).read().split('\n\n')
    rules = [[int(s) for s in line.split('|')] for line in data[0].splitlines()]
    updates = [[int(s) for s in line.split(',')] for line in data[1].splitlines()]
    print(len(rules))
    print(len(updates))

    for updates_block in updates:
        print('Updates block: {}'.format(updates_block))
        max_index = len(updates_block)-1
        page_index = 0
        rule_broken = False
        for page in updates_block:
            for rule in rules:
                if page == rule[0]:
                    # print("RULEMATCH: This page must be BEFORE {} <- {}".format(page, rule[1]))
                    # Scan if left of us ISN'T the other page number
                    for i in range(page_index):
                        if rule[1] == updates_block[i]:
                            print("RULEBREAK: page [ {} ] isn't BEFORE <- [ {} ]".format(page, rule[1]))
                            rule_broken = True
                            # Fix the order based on rules
                            # move current page to this index i
                            updates_block.insert(i, updates_block.pop(page_index))
                            break
                elif page == rule[1]:
                    # print("RULEMATCH: This page must be AFTER  {} -> {}".format(page, rule[0]))
                    # Scan if right of us ISN'T the other page number
                    for i in range(page_index, len(updates_block)-1):
                        if rule[0] == updates_block[i]:
                            print("RULEBREAK: page [ {} ] isn't AFTER  -> [ {} ]".format(page, rule[0]))
                            # Fix the order based on rules
                            # move current page to this index i
                            updates_block.insert(i, updates_block.pop(page_index))
                            rule_broken = True
                            break
            page_index+=1
        if rule_broken:
            # we assume we fixed it above and only need to grab the mid termin value.
            result_index = int((len(updates_block)-1)/2)
            print('Invalid Update mid: [{}]'.format(updates_block[result_index]))
            result += updates_block[result_index]
    return result

if __name__ == "__main__":
    # print(sum_mid_page_updates(sample_file))
    # print(sum_mid_page_updates(input_file))
    print(fix_and_sum_mid_page_updates(sample_file))
    # print(fix_and_sum_mid_page_updates(input_file))
