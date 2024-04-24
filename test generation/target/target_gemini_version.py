import random

def generate_grid() -> list[list[str]]:
  """
  Generates a list of lists representing the game board with a balanced vowel distribution.
  """
  vowels = 'aeiou'
  consonants = 'bcdfghjklmnpqrstvwxyz'
  grid = []
  for _ in range(3):
    row = random.sample(vowels, 1) + random.sample(consonants, 2)
    random.shuffle(row)
    grid.append(row)
  return grid

def get_words(f: str, letters: list[str]) -> list[str]:
  """
  Reads words from a file, checks if they can be built from the board letters,
  and returns a list of valid words.
  """
  words = []
  center_letter = letters[4].lower()
  with open(f, 'r') as file:
    for line in file:
      word = line.strip().lower()
      if len(word) >= 4 and all(word.count(c) <= letters.count(c) for c in word) and center_letter in word:
        words.append(word)
  return words

def get_user_words() -> list[str]:
  """
  Gets words from user input until Ctrl+D (Linux/Mac) or Ctrl+Z+Enter (Windows) is pressed.
  """
  user_words = []
  while True:
    word = input("Enter a word (Ctrl+D/Ctrl+Z to finish): ").strip().lower()
    if not word:
      break
    user_words.append(word)
  return user_words

def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
  """
  Checks user words against the rules and returns words not found in the dictionary.
  """
  valid_user_words = [word for word in user_words if len(word) >= 4 and all(word.count(c) <= letters.count(c) and letters[4] in word for c in word)]
  return [word for word in valid_user_words if word not in words_from_dict]

def main():
  """
  Main function that runs the Target game.
  """
  grid = generate_grid()
  print("Game board:")
  for row in grid:
    print(" ".join(row))

  user_words = get_user_words()

  words_from_dict = get_words("en.txt", sum(grid, []))
  correct_words = [word for word in user_words if word in words_from_dict]
  incorrect_words = [word for word in words_from_dict if word not in user_words]
  pure_incorrect_words = get_pure_user_words(user_words, sum(grid, []), words_from_dict)

  print(f"\nYou found {len(correct_words)} correct words:")
  for word in correct_words:
    print(word)

  print(f"\nThese words are in the dictionary but you missed them:")
  for word in incorrect_words:
    print(word)

  if pure_incorrect_words:
    print(f"\nThese words you entered are not in the dictionary:")
    for word in pure_incorrect_words:
      print(word)

if __name__ == "__main__":
  main()
