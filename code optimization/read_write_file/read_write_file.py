import urllib.request

def read_input_file(url_link: str, number: int) -> list[list[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url
    
    >>> read_input_file \
('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file ('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    with urllib.request.urlopen(url_link) as file:
        file = file.readlines()
    file = [line.decode('utf-8').strip() for line in file]

    if number == 0:
        return []

    grade_ = []
    res = []

    plus_ = [line.split('\t')[1] for line in file if line.startswith('—')]
    grade_ = [line.split()[-1] for line in file if line.startswith('Середній')]
    lines = [line.split('\t') for line in file if line[0].isdigit()]
    res = [[line[0], line[1], plus_[i], line[3], grade_[i]] for i, line in enumerate(lines) if i < number]

    return res

def write_csv_file(url: str):
    """
    str -> csv
    """
    with open("total.csv", "w", encoding= "utf-8") as result:
        start_line = "№,ПІБ,Д,Заг.бал,С.б.док.осв."
        result.write(start_line)
        for line in read_input_file(url, 77):
            result.write("\n" + ",".join(line))

