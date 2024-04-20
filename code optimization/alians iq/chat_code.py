import time
import random
import string
from memory_profiler import profile
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
    if smarties:
            sort_smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
            sort_smarties = dict(sorted(sort_smarties.items(), key=lambda x: (-x[1], x[0])))
            travels = []
            temp_iq = limit_iq
            while sort_smarties:
                current_travels = []
                remaining_smarties = {}
                for name, iq in sort_smarties.items():
                    if temp_iq >= iq:
                        current_travels.append(name)
                        temp_iq -= iq
                    else:
                        remaining_smarties[name] = iq
                travels.append(current_travels)
                sort_smarties = remaining_smarties
                temp_iq = limit_iq
            return len(travels), travels
    return 0, []

def create_dict():
    num_keys = 100000
    value_range = (100, 400) 
    random_dict = {}
    for _ in range(num_keys):
        random_key = ''.join(random.choices(string.ascii_uppercase, k=2))
        random_value = random.randint(value_range[0], value_range[1])
        random_dict[random_key] = random_value
    return random_dict



def test_time():
    start_time = time.time()
    
    rescue = rescue_people(create_dict(), 600)

    end_time = time.time()
    print(f'Execution time: {end_time - start_time}')


test_time()


