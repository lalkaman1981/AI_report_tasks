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
    valid_words = set()
    
    with open(f, 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) >= 4 and center_letter in word and all(word.count(char) <= letters.count(char) for char in word):
                valid_words.add(word.capitalize())
    
    return list(valid_words)

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    missed_words = [word for word in words_from_dict if word not in user_words]
    invalid_user_words = [word for word in user_words if word not in words_from_dict]
    
    return missed_words, invalid_user_words

def main():
    grid = generate_grid()
    letters = [char for row in grid for char in row]
    
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

