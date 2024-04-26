import unittest
from sort_songs_gpt import sort_songs, song_length, title_length, last_word

class TestSortSongs(unittest.TestCase):
    def test_song_length(self):
        # Test song_length function
        self.assertEqual(song_length(('Song A', '3.19')), 3.19)

    def test_title_length(self):
        # Test title_length function
        self.assertEqual(title_length(('Song A', '3.19')), 6)  # 'Song A' has length 6

    def test_last_word(self):
        # Test last_word function
        self.assertEqual(last_word(('Hello World', '3.19')), 'World')  # Last word is 'World'

    def test_sort_songs_song_length(self):
        # Test sorting by song length
        song_titles = ['Song A', 'Song B', 'Song C']
        length_songs = ['3.19', '3.58', '5.06']
        expected_result = [('Song A', '3.19'), ('Song B', '3.58'), ('Song C', '5.06')]
        result = sort_songs(song_titles, length_songs, song_length)
        self.assertEqual(result, expected_result)

    def test_sort_songs_title_length(self):
        # Test sorting by title length
        song_titles = ['Song A', 'Song BB', 'Song CCC']
        length_songs = ['3.19', '3.58', '5.06']
        expected_result = [('Song A', '3.19'), ('Song BB', '3.58'), ('Song CCC', '5.06')]
        result = sort_songs(song_titles, length_songs, title_length)
        self.assertEqual(result, expected_result)

    def test_sort_songs_last_word(self):
        # Test sorting by last word
        song_titles = ['Hello World', 'Python Programming', 'OpenAI ChatGPT']
        length_songs = ['3.19', '3.58', '5.06']
        expected_result = [('OpenAI ChatGPT', '5.06'), ('Python Programming', '3.58'), ('Hello World', '3.19')]
        result = sort_songs(song_titles, length_songs, last_word)
        self.assertEqual(result, expected_result)

    def test_sort_songs_invalid_input(self):
        # Test sorting with invalid input
        # Testing with different length lists
        song_titles = ['Song A', 'Song B', 'Song C']
        length_songs = ['3.19', '3.58']  # Different length
        result = sort_songs(song_titles, length_songs, song_length)
        self.assertIsNone(result)

        # Testing with empty lists
        song_titles = []
        length_songs = []
        result = sort_songs(song_titles, length_songs, song_length)
        self.assertIsNone(result)

