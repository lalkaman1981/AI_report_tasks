#THISI IS MY ORIGINAL CODE


"""Calculates the equasion given as expression"""
def calculate_expression(expression:str) -> int:
    """
    >>> calculate_expression ('Скільки буде 5 додати 5?')
    10
    >>> calculate_expression ('Скільки буде 2 помножити на 10 додати 7?')
    27
    >>> calculate_expression ('Скільки буде 2 додати 10 помножити на 7?')
    84
    >>> calculate_expression ('Скільки буде 3 в квадраті?')
    'Неправильний вираз!'
    >>> calculate_expression ('Скільки сезонів в році?')
    'Неправильний вираз!'
    >>> calculate_expression ('Скільки буде 2 2 додати?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 поділити на 2')
    5
    """

    if isinstance(expression, str) and expression.endswith('?'):
        expression = expression.replace('?', '')
        expression = expression.split()
        n = 0
        c = 0
        m = 0
        allowed = ['Скільки','буде','додати','плюс','відняти','мінус','помножити','поділити','на']
        for i, word in enumerate(expression):
            try:
                num = int(word)
            except ValueError:
                if (word in allowed) and (expression[i-1].isnumeric or expression[i-1] == 'помножити' or expression[i-1] == 'Скільки' or expression[i-1] == 'поділити'):
                    c += 1
                else:
                    return 'Неправильний вираз!'
            else:
                if c>0:
                    num = int(word)
                    if expression[i-2] == 'Скільки' and expression[i-1] == 'буде':
                        n += num
                    elif expression[i-1] == 'додати' or expression[i-1] == 'плюс':
                        n += num
                    elif expression[i-1] == 'відняти' or expression[i-1] == 'мінус':
                        n -= num
                    elif expression[i-2] == 'помножити' and expression[i-1] == 'на':
                        n = n*num
                    elif expression[i-2] == 'поділити' and expression[i-1] == 'на':
                        n = n/num
                    else:
                        return 'Неправильний вираз!'
                    c = 0
                    m +=1
                else:
                    return "Неправильний вираз!"
        if m == 0:
            return 'Неправильний вираз!'
        else:
            return n
    else:
        return 'Неправильний вираз!'


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
