def parse_input(input_string):
    lines = input_string.strip().split('\n')
    return [list(map(int, line.split())) for line in lines]

def chkSafeOrUnsafe(input_data):
    res = 0
    arr = parse_input(input_data)
    
    for report in arr:
        isIncreasing = None
        isSafe = True
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if abs(diff) < 1 or abs(diff) > 3:
                isSafe = False
                break
            if isIncreasing is None:
                isIncreasing = diff > 0
            if (isIncreasing and diff < 0) or (not isIncreasing and diff > 0):
                isSafe = False
                break
        if isSafe:
            res += 1
    return res

def checkSafety(report):
    isIncreasing = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if isIncreasing is None:
            isIncreasing = diff > 0
        elif (isIncreasing and diff < 0) or (not isIncreasing and diff > 0):
            return False
    return True

def chkSafeOrUnsafeByRemovingLevel(input_data):
    res = 0
    arr = parse_input(input_data)

    for report in arr:
        isSafe = checkSafety(report=report)

        if not isSafe:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if checkSafety(modified_report):
                    isSafe = True
                    break;
        if isSafe:
            res += 1
    return res

def solve_part_1(input_data):
    return chkSafeOrUnsafe(input_data)

def solve_part_2(input_data):
    return chkSafeOrUnsafeByRemovingLevel(input_data)
