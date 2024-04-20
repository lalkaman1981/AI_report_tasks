"""
Working with files, feat. Nazar Melnyk 
"""
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
    if 0 < number <= 77 and isinstance(url_link, str) and isinstance(number, int):
        grade_ = []
        res = []
        plus_ = []
        num_ = []
        name_ =[]
        nmt_ = []
        result = []
        length = len(file)
        for i in range(length):
            if file[i][0] == '—':
                plus_.append(" ".join(file[i].split('\t')[1:2]))
            if file[i].split()[0] == 'Середній':
                grade_.append(" ".join([file[i].split()[-1]]))
            if file[i][0].isdigit():
                name_.append(" ".join(file[i].split('\t')[1:2]))
                num_.append(" ".join(file[i].split('\t')[:1]))
                nmt_.append(" ".join(file[i].split('\t')[3:4]))
        for j in range(len(num_)):
            result += num_[j], name_[j], plus_[j], nmt_[j], grade_[j]

        for t in range(0, len(result), 5):
            s = result[t:t + 5]
            res.append(s)
        res = res[:number]
        return res

def write_csv_file(url: str):
    """
    str -> csv
    """
    with open("total.csv", "w", encoding= "utf-8") as result:
        start_line = "№,ПІБ,Д,Заг.бал,С.б.док.осв."
        result.write(start_line)
        for i in read_input_file(url, 77):
            new_list = "\n"+",".join(i)
            result.write(new_list)
