"""
Function read_file(file_path) accepts the path to the
corresponding file file_path and returns a dictionary 
whose keys should be the names and surnames of people 
in the form of a single string, and the values are 
their IQ level of type int. Function rescue_people(smarties,
limit_iq) accepts a dictionary of smarties of people to be evacuated 
by the aliens (gets it as a result of the read_file function), 
and limit_iq - the limit of the total IQ of people who can be on board 
The return value of this function is a tuple of the number of 
required trips and a list of lists, where each inner list 
represents a trip and contains the names of the people transported 
on that trip in the order they were chosen by the aliens.
"""
def read_file(file_path: str) -> dict:
    """
    str -> dict

    Accepts the path to the corresponding file file_path 
    and returns a dictionary whose keys should be the names 
    and surnames of people in the form of a single string, 
    and the values are their IQ level of type int.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w',delete=False) as tmp:
    ...     _=tmp.write('AB,200\\nBC,200\\nID,250\\nIB,250\\nOC,300\\nOD,300\\ni,350')
    >>> read_file(tmp.name)
    {'AB': 200, 'BC': 200, 'ID': 250, 'IB': 250, 'OC': 300, 'OD': 300, 'i': 350}
    """
    dict_smart_people = {}
    with open(file_path, 'r', encoding='utf-8') as smart_pl_info:
        for line in smart_pl_info:
            if line[0].isalpha():
                line_edit = line.strip().split(',')
                dict_smart_people[line_edit[0]] = int(line_edit[1])
    return dict_smart_people
def rescue_people(smarties: dict, limit_iq: int) -> tuple:
    """
    (dict, int) -> tuple

    Accepts a dictionary of smarties of people to be evacuated 
    by the aliens (gets it as a result of the read_file function), 
    and limit_iq - the limit of the total IQ of people who can be on board 
    The return value of this function is a tuple of the number of 
    required trips and a list of lists, where each inner list 
    represents a trip and contains the names of the people transported 
    on that trip in the order they were chosen by the aliens.
    >>> print(rescue_people({'AB': 200, 'BC': 200, 'ID': \
250, 'IB': 250, 'OC': 300, 'OD': 300, 'i': 350}, 500))
    (4, [['i'], ['OC', 'AB'], ['OD', 'BC'], ['IB', 'ID']])
    >>> print(rescue_people({'BC': 200, 'ID': \
250, 'IB': 250, 'OC': 300, 'OD': 300, 'i': 350}, 400))
    (6, [['i'], ['OC'], ['OD'], ['IB'], ['ID'], ['BC']])
    """
    if smarties:
        stupid = [name for name, iq in smarties.items() if iq < 130]
        for i in stupid:
            smarties.pop(i)
        sort_smarties = dict(sorted(smarties.items(), key= lambda x: x[1], reverse=True))
        travels = []
        temp_travels = []
        temp_iq = limit_iq
        temp_dict = sort_smarties.copy()
        while True:
            set_check = set(sort_smarties.values())
            if len(set_check) == 1:
                sort_smarties = dict(sorted(sort_smarties.items()))
            for name, iq in sort_smarties.items():
                if temp_iq >= iq:
                    temp = sort_smarties.copy()
                    temp.pop(name)
                    if iq in temp.values():
                        dublicate_list = [name for name, iq1 in temp_dict.items() if iq == iq1]
                        dubl = sorted(dublicate_list)
                        temp_travels.append(dubl[0])
                        temp_iq -= iq
                        temp_dict.pop(dubl[0])
                    else:
                        temp_travels.append(name)
                        temp_iq -= iq
            temp_iq = limit_iq
            travels.append(temp_travels)
            for name in temp_travels:
                sort_smarties.pop(name)
            temp_travels = []
            if sort_smarties:
                set_check = set(sort_smarties.values())
                if len(set_check) == 1:
                    sort_smarties = dict(sorted(sort_smarties.items()))
            else:
                break
        return (len(travels), travels)
    return (0, [])
    