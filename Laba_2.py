def evaluate_expression(expression):
    def apply_operation(operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("Division by zero")
            return operand1 / operand2

    def greater_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedences[op1] > precedences[op2]

    def fool_check(expression):
        open_brackets = 0
        for char in expression[:-1]:
            if char == '(':
                open_brackets += 1
            elif char == ')':
                open_brackets -= 1
                if open_brackets < 0:
                    return False
        return open_brackets == 0

    if not fool_check(expression):
        raise ValueError("Mismatched brackets")

    operators = []
    operands = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i + 1
            while j < len(expression) and expression[j].isdigit():
                j += 1
            operands.append(float(expression[i:j]))
            i = j
        elif expression[i] in "+-*/":
            while operators and operators[-1] != '(' and greater_precedence(operators[-1], expression[i]):
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(apply_operation(operand1, operand2, operator))
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(apply_operation(operand1, operand2, operator))
            operators.pop()
            i += 1
        elif expression[i] == '=':
            while operators:
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(apply_operation(operand1, operand2, operator))
            i += 1
        else:
            raise ValueError("Invalid character")

    result = operands[0]
    return result


expression = input("Enter the expression: ")
try:
    print(evaluate_expression(expression))
except ValueError as e:
    print(e)