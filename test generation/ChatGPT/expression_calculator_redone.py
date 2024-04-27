from collections import deque

def calculate_expression(expression:str):
    if not expression.strip().startswith('Скільки буде') or not expression.strip().endswith('?'):
        return 'Неправильний вираз!'

    operators = {
        'додати':'+',
        'плюс':'+',
        'відняти':'-',
        'мінус':'-',
        'поділити на':'/',
        'помножити на':'*',
    }
    for text, op in operators.items():
        expression = expression.replace(text, op)

    expression = expression.strip('? \n')
    expression_lst = expression.strip('? \n').split(' ')
    deq = deque()
    for item in expression_lst:
        if item.isnumeric() or item[1:].isnumeric():
            deq.append(int(item))
        elif item in operators.values():
            deq.append(item)

    if len(deq) == 1:
        res = deq.pop()
        return res if isinstance(res, int) and str(res) == expression_lst[-1] else 'Неправильний вираз!'

    if len(deq) < 3:
        return 'Неправильний вираз!'
    

    while len(deq) > 2:
        first = deq.popleft()
        operator = deq.popleft()
        second = deq.popleft()
        if not isinstance(first, int) \
            or not isinstance(second, int) \
            or operator not in operators.values():
            return 'Неправильний вираз!'

        match operator:
            case '+':
                result = first + second
            case '-':
                result = first - second
            case '*':
                result = first*second
            case '/':
                if second:
                    result = first/second
                else:
                    return 'Неправильний вираз!'
        deq.appendleft(int(result))

    res = deq.pop()
    return res if isinstance(res, int) else 'Неправильний вираз!'


print(calculate_expression('Скільки буде 8 додати 3 ?'))