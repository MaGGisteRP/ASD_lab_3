def check_brackets(expression):
    stack = []
    open_brackets = ["(", "{", "["]
    close_brackets = [")", "}", "]"]

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0:
                return "Строка не существует"
            last_open_bracket = stack.pop()
            if open_brackets.index(last_open_bracket) != close_brackets.index(char):
                return "Строка не существует"

    if len(stack) == 0:
        return "Строка существует"
    else:
        return "Строка не существует"

expression = input("Введите строку: ")
result = check_brackets(expression)
print(result)
