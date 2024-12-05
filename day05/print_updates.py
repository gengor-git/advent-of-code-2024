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
    data = open(data_file).read().split('\n\n')
    rules = [[int(s) for s in line.split('|')] for line in data[0].splitlines()]
    updates = [[int(s) for s in line.split(',')] for line in data[1].splitlines()]
    print('# update blocks: {}'.format(len(updates)))
    # print(updates)
    print('# rules: {}'.format(len(rules)))
    print(rules)

    for idx_u, update in enumerate(updates):
        print('{:>4} : {}'.format(idx_u, update))
        fixed_it = False        
        for idx_r, rule in enumerate(rules):
            try:
                current_page_idx = update.index(rule[0])
                should_be_right_idx = update.index(rule[1])

                if current_page_idx > should_be_right_idx:
                    print('R:Should be \033[93m[{}][{}]\x1b[0m but was \033[0;35;40m{}\033[0m'.format(rule[0], rule[1], update))
                    # switch places
                    update.insert(should_be_right_idx, update.pop(current_page_idx))
                    print('                         now \033[0;35;94m{}\x1b[0m'.format(update))
                    fixed_it = True
            except ValueError:
                pass
            try:
                should_be_left_idx = update.index(rule[0])
                current_page_idx = update.index(rule[1])

                if current_page_idx < should_be_left_idx:
                    print('L:Should be \033[93m[{}][{}]\x1b[0m but was \033[0;35;40m{}\033[0m'.format(rule[0], rule[1], update))
                    # switch places
                    update.insert(should_be_left_idx+1, update.pop(current_page_idx))
                    print('                         now \033[0;35;94m{}\x1b[0m'.format(update))
                    fixed_it = True
            except ValueError:
                pass
        print('-{:>3} : \033[3;40;41m{}\033[0m'.format(idx_u, update))

        # for idx_p, page in enumerate(update):
            # print('    \_ {:>4} : {}'.format(idx_p, page))

        if fixed_it:
            result_index = int((len(update)-1)/2)
            print('               \x1b[6;30;42m[{}]\x1b[0m'.format(update[result_index]))
            result += update[result_index]

    return result

if __name__ == "__main__":
    # print(sum_mid_page_updates(sample_file))
    # print(sum_mid_page_updates(input_file))
    print(fix_and_sum_mid_page_updates(sample_file))
    # print(fix_and_sum_mid_page_updates(input_file))
