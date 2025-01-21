def parse_input():
    first = []
    second = []
    with open ("./data.text", "r") as file:
        results = []
        for line in file:
            line = line.replace("\n" , "")
            splits = line.split(" ")
            results.append(splits)
        return results

def is_diff_safe(diff):
    if abs(diff) > 0 and abs(diff) < 4:

        return True
    print(f"failing becasue gap between numbers was two big {abs(diff)}")
    return False

def is_change_direction_uniform(diff1, diff2):
    if diff1 > 0 and diff2 > 0:
        return True
    if diff1 < 0 and diff2 < 0:
        return True
    print(f"failing becasue direction changed{diff1} {diff2}")
    return False


def are_levels_safe(levels, element_removed_already):
    # starting with the 3rd element look through each element and compare it to the previous 2 elements
    for i in range(2, len(levels)):
        element = int(levels[i])
        element_minus_1 =  int(levels[i-1])
        element_minus_2 = int(levels[i-2])
        diff1 = element_minus_2 - element_minus_1
        diff2 = element_minus_1 - element
        changes_safe =  is_diff_safe(diff1) and  is_diff_safe(diff2)
        if changes_safe and is_change_direction_uniform(diff1, diff2):
            continue
        
        if element_removed_already:
            return False
        # try removing each of element
        option1 = levels[:(i-2)] + levels[(i-2)+1:]
        option2 = levels[:(i-1)] + levels[(i-1)+1:]
        option3 = levels[:(i)] + levels[(i)+1:]
        

        return are_levels_safe(option1, True) or are_levels_safe(option2, True) or are_levels_safe(option3, True)
    return True

results = parse_input()
safe = 0
for result in results:
    print(result)
    if are_levels_safe(result, False):
        safe += 1
    print (safe)
