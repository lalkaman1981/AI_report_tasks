import random

def generate_grid() -> list[list[str]]:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    num_vowels = 3
    num_consonants = 6
    
    grid = []
    for _ in range(3):
        row = []
        for _ in range(3):
            if num_vowels > 0:
                char = random.choice(vowels)
                num_vowels -= 1
            else:
                char = random.choice(consonants)
                num_consonants -= 1
            row.append(char.upper())
        grid.append(row)
    
    return grid

def get_user_words() -> list[str]:
    user_words = []
    print("Enter words (minimum 4 letters, press Ctrl+D (Unix) or Ctrl+Z+Enter (Windows) to finish):")
    try:
        while True:
            word = input().strip().lower()
            if len(word) >= 4:
                user_words.append(word)
    except EOFError:
        pass
    
    return user_words

def get_words(f: str, letters: list[str]) -> list[str]:
    center_letter = letters[4].lower()  # Central letter is at index 4 (0-based index)
    valid_words = []
    
    with open('en.txt', 'r') as file:
        for word in file.readlines()[3:]:
            word_strip = word.strip().lower()
            if len(word_strip) >= 4 and center_letter in word_strip and all(word_strip.count(char) <= letters.count(char) for char in word_strip):
                valid_words.append(word_strip)
    
    return list(valid_words)

def is_valid_word(word: str, letters: list[str], center_letter: str) -> bool:
    # Check if word is valid based on game rules
    if len(word) < 4 or center_letter not in word:
        return False
    
    letter_counts = {char: letters.count(char) for char in letters}
    word_counts = {char: word.count(char) for char in set(word)}
    
    for char in word_counts:
        if word_counts[char] > letter_counts.get(char, 0):
            return False
    
    return True

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    center_letter = letters[4].lower()  # Central letter is at index 4 (0-based index)
    valid_user_words = [word for word in user_words if is_valid_word(word, letters, center_letter)]
    
    missed_words = [word for word in valid_user_words if word not in words_from_dict]
    
    return missed_words

def main():
    grid = generate_grid()
    letters = [char.lower() for row in grid for char in row]
    
    print("Game board:")
    for row in grid:
        print(' '.join(row))
    
    user_words = get_user_words()
    words_from_dict = get_words('en.txt', letters)
    
    print("\nWords formed from the grid:")
    for word in words_from_dict:
        print(word)
    
    missed_words, invalid_user_words = get_pure_user_words(user_words, letters, words_from_dict)
    
    print("\nWords in dictionary but missed by the player:")
    for word in missed_words:
        print(word)
    
    print("\nWords entered by the player but not in the dictionary or with errors:")
    for word in invalid_user_words:
        print(word)
print(get_pure_user_words(['seva', 'seht', 'sera', 'sare', 'ltr', 'qrt', 'g', 'wwwww', 'rtgf', 'sxdl', 'sedl', 'tsal'],
 'vhtdsrael', get_words('en.txt', 'vhtdsrael')))
