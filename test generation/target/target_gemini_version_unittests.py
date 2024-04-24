import unittest
from target_gemini_version import generate_grid, get_words, get_pure_user_words

class TestTargetFunctions(unittest.TestCase):

  def test_generate_grid(self):
    """
    Tests if generate_grid returns a 3x3 list with 3 vowels and 6 consonants.
    """
    grid = generate_grid()
    self.assertEqual(len(grid), 3)
    self.assertEqual(len(grid[0]), 3)
    vowels = 0
    consonants = 0
    for row in grid:
      for letter in row:
        if letter in 'aeiou':
          vowels += 1
        else:
          consonants += 1
    self.assertEqual(vowels, 3)
    self.assertEqual(consonants, 6)

  def test_get_words(self):
    """
    Tests if get_words returns valid words from a mock dictionary.
    """
    grid = generate_grid()
    letters = sum(grid, [])  # Flatten the grid into a single list of letters
    valid_words = get_words("en.txt", letters)  # Assuming "en.txt" is your dictionary file
    for word in valid_words:
        self.assertTrue(len(word) >= 4)

  def test_get_pure_user_words(self):
    """
    Tests get_pure_user_words to identify valid user words not in the dictionary.
    """
    user_words = ['tesap']
    letters = ['t', 'o', 'n', 
               's', 'e', 'a', 
               'b', 'c', 'p']
    words_from_dict = ['tone', 'test']
    pure_words = get_pure_user_words(user_words, letters, words_from_dict)
    self.assertEqual(pure_words, ['tesap'])

if __name__ == '__main__':
  unittest.main()
