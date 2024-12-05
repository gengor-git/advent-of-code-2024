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
    print('# update blocks: {}'.format(len(updates)))
    print(updates)
    print('# rules: {}'.format(len(rules)))
    print(rules)


    for update in updates:
        print('================================================\nUpdates block:   {}'.format(update))
        max_index = len(update)-1
        # current_page_index = 0
        rule_was_broken = False
        current_page_index = 0
        while current_page_index < len(update):
            print('Current     page [ {} ] [ {} ]'.format(current_page_index, update[current_page_index]))
            # print("Applying rules")
            for rule in rules:
                if update[current_page_index] == rule[0]:
                    # Scan if left of us ISN'T the other page number
                    for i in range(current_page_index):
                        if rule[1] == update[i]:
                            print("RULEBREAK   page [ {} ] [ {} ] isn't BEFORE <- [ {} ]".format(current_page_index, update[current_page_index], rule[1]))
                            rule_was_broken = True
                            # Fix the order based on rules
                            # move current page to this index i
                            update.insert(i, update.pop(current_page_index))
                            print('New updates block: {}'.format(update))
                elif update[current_page_index] == rule[1]:
                    # Scan if right of us ISN'T the other page number
                    for i in range(current_page_index+1, len(update)):
                        if rule[0] == update[i]:
                            print("RULEBREAK   page [ {} ] [ {} ] isn't AFTER  -> [ {} ]".format(current_page_index, update[current_page_index], rule[0]))
                            # Fix the order based on rules
                            # move current page to this index i
                            update.insert(i, update.pop(current_page_index))
                            print('Fixed page order {}'.format(update))
                            rule_was_broken = True
            if not rule_was_broken:
                current_page_index += 1
            else:
                current_page_index += 1
        if rule_was_broken:
            # we assume we fixed it above and only need to grab the mid termin value.
            result_index = int((len(update)-1)/2)
            print('================================================\nInvalid Update mid: [{}]'.format(update[result_index]))
            result += update[result_index]
    return result

if __name__ == "__main__":
    # print(sum_mid_page_updates(sample_file))
    # print(sum_mid_page_updates(input_file))
    # print(fix_and_sum_mid_page_updates(sample_file))
    print(fix_and_sum_mid_page_updates(input_file))
