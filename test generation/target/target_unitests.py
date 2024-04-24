import unittest
import target  # Import the module containing game functions

class TestTargetGame(unittest.TestCase):
    
    def test_generate_grid(self):
        # Test generate_grid() function
        grid = target.generate_grid()
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 3)
        for row in grid:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 3)
            for char in row:
                self.assertTrue(char.isalpha() and char.isupper())
    
    def test_get_words(self):
        # Test get_words() function with different sets of letters 
        letters1 = ['e', 't', 'o', 'o', 'p', 'n', 'p', 'u', 'r']
        words1 = target.get_words('en.txt', letters1)
        self.assertIsInstance(words1, list)
        self.assertTrue(all(isinstance(word, str) for word in words1))
        
        letters2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        words2 = target.get_words('en.txt', letters2)
        self.assertIsInstance(words2, list)
        self.assertTrue(all(isinstance(word, str) for word in words2))
    
    def test_is_valid_word(self):
        # Test is_valid_word() function with different word, letters, and center letter combinations
        letters = ['v', 'h', 't', 'd', 's', 'r', 'a', 'e', 'l']
        center_letter = 's'
        valid_word = 'starved'
        invalid_word = 'trasheñ'
        
        self.assertTrue(target.is_valid_word(valid_word, letters, center_letter))
        self.assertFalse(target.is_valid_word(invalid_word, letters, center_letter))
    
    def test_get_pure_user_words(self):
        # Test get_pure_user_words() function with user words, letters, and words from the dictionary
        user_words = ['star', 'stave', 'deals', 'thread', 'heart']
        letters = ['v', 'h', 't', 'd', 's', 'r', 'a', 'e', 'l']
        words_from_dict = ['star', 'deals', 'thread']
        
        missed_words = target.get_pure_user_words(user_words, letters, words_from_dict)
        self.assertIsInstance(missed_words, list)
        self.assertTrue(all(isinstance(word, str) for word in missed_words))
    
if __name__ == "__main__":
    unittest.main()
