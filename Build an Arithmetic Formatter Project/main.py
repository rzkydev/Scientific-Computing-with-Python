def arithmetic_arranger(problems, show_answers=False):
    # Error 1: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []

    for problem in problems:
        parts = problem.split()

        # Error 2: Operator must be '+' or '-'.
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Error 3: Numbers must only contain digits.
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Error 4: Numbers cannot be more than four digits.
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]

        # Determine the width of the formatted problem
        width = max(len(operand1), len(operand2)) + 2

        # Format each part
        top_line.append(operand1.rjust(width))
        bottom_line.append(operator + operand2.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            result_line.append(result.rjust(width))

    # Combine all parts with 4 spaces in between
    arranged_problems = '    '.join(top_line) + '\n' + \
                        '    '.join(bottom_line) + '\n' + \
                        '    '.join(dash_line)

    if show_answers:
        arranged_problems += '\n' + '    '.join(result_line)

    return arranged_problems


# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
