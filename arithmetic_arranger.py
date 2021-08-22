def arithmetic_arranger(problems, solve=True):
    opperands_above = list()
    opperands_below = list()
    top = ''
    bottom = ''
    lines = ''
    result = ''
    math = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for x in problems:
        y = x.split()
        opperands_above.append(y[0])
        opperands_below.append(y[2])
        for x in opperands_above:
            if len(x) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if x.isnumeric() == False:
                return 'Error: Numbers must only contain digits.'
        for x in opperands_below:
            if len(x) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if x.isnumeric() == False:
                return 'Error: Numbers must only contain digits.'
        first = y[0]
        second = y[2]
        operator = y[1]
        length = max(len(first), len(second))+2
        top += str(first.rjust(length))
        bottom += str(operator + second.rjust(length-1))
        for a in range(length):
            lines += '-'
        if operator == '+':
            math = str(int(first) + int(second))
        elif operator == '-':
            math = str(int(first) - int(second))
        else:
            return "Error: Operator must be '+' or '-'."

        result += str(math.rjust(length))
        if x is not problems[-1]:
            top = top + '  '
            bottom = bottom + '  '
            lines = lines + '  '
            result = result + '  '
    if solve:
        arranged_problems = top + '\n' + bottom + '\n' + lines + '\n' + result
    else:
        arranged_problems = top + '\n' + bottom + '\n' + lines

    return arranged_problems
