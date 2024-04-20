import urllib.request

def read_input_file(url_link: str, number: int) -> list[list[str]]:
  """
  (str, int) -> (list(list))
  Preconditions: 0 <= number <= 77

  Return list of strings lists from url

  >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt', 1)
  [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
  >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt', 3)
  [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
  """

  with urllib.request.urlopen(url_link) as file:
    lines = file.readlines()

  if number == 0:
    return []

  if 0 < number <= 77 and isinstance(url_link, str) and isinstance(number, int):
    result = []
    for line in lines:
      decoded_line = line.decode('utf-8').strip()
      if not decoded_line:  # Skip empty lines for efficiency
        continue

      if decoded_line[0] == '—':
        plus = " ".join(decoded_line.split('\t')[1:2])
      elif decoded_line.split()[0] == 'Середній':
        grade = " ".join([decoded_line.split()[-1]])
      elif decoded_line[0].isdigit():
        num, name = " ".join(decoded_line.split('\t')[:2]).split(' ', 1)
        nmt = " ".join(decoded_line.split('\t')[3:4])
        result.append([num, name, plus, nmt, grade])

  return result[:number]


def write_csv_file(url: str):
  """
  str -> csv
  """
  data = read_input_file(url, 77)

  with open("total.csv", "w", encoding="utf-8") as result:
    start_line = "№,ПІБ,Д,Заг.бал,С.б.док.осв."
    result.write(start_line)
    for line in data:
      new_line = "\n" + ",".join(line)
      result.write(new_line)

