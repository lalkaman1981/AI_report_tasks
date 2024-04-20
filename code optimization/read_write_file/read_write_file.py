import urllib.request

def read_input_file(url_link: str, number: int) -> list[list[str]]:
    """
    (str, int) -> (list[list]])
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url
    """
    if not (isinstance(url_link, str) and isinstance(number, int) and 0 <= number <= 77):
        raise ValueError("Invalid input")
    
    with urllib.request.urlopen(url_link) as file:
        lines = file.readlines()
        
    data = []
    for line in lines:
        line = line.decode('utf-8').strip()
        if line[0].isdigit() or line[0] == '—':
            data.append(line.split('\t'))
    
    return data[:number]

def write_csv_file(url: str):
    """
    str -> csv
    """
    with open("total.csv", "w", encoding="utf-8") as result:
        start_line = "№,ПІБ,Д,Заг.бал,С.б.док.осв."
        result.write(start_line)
        for i in read_input_file(url, 77):
            new_list = "\n"+",".join(i)
            result.write(new_list)

