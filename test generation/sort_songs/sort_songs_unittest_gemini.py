import unittest

from sort_songs_gemini import song_length, title_length, last_word, sort_songs


class TestSortSongs(unittest.TestCase):

    def test_song_length_function(self):
        """Tests the song_length function with valid input."""
        song_data = ("Song Title", "3.14")
        expected_length = 3.14
        actual_length = song_length(song_data)
        self.assertEqual(actual_length, expected_length)

    def test_title_length_function(self):
        """Tests the title_length function with valid input."""
        song_data = ("This is a Long Title", "4.20")
        expected_length = 20
        actual_length = title_length(song_data)
        self.assertEqual(actual_length, expected_length)

    def test_last_word_function(self):
        """Tests the last_word function with valid input."""
        song_data = ("Another Song", "5.00")
        expected_word = "S"
        actual_word = last_word(song_data)
        self.assertEqual(actual_word, expected_word)

    def test_sort_songs_by_length(self):
        """Tests sorting songs by song length."""
        song_titles = ["Song 1", "Song 2", "Song 3"]
        length_songs = ["2.30", "4.15", "1.50"]
        expected_sorted = [
            ("Song 3", "1.50"),
            ("Song 1", "2.30"),
            ("Song 2", "4.15"),
        ]
        sorted_songs = sort_songs(song_titles, length_songs, song_length)
        self.assertEqual(sorted_songs, expected_sorted)

    def test_sort_songs_by_title_length(self):
        """Tests sorting songs by title length."""
        song_titles = ["Short Song", "This is a Long Song", "Medium Song"]
        length_songs = ["3.00", "5.20", "4.00"]
        expected_sorted = [
            ("Short Song", "3.00"),
            ("Medium Song", "4.00"),
            ("This is a Long Song", "5.20"),
        ]
        sorted_songs = sort_songs(song_titles, length_songs, title_length)
        self.assertEqual(sorted_songs, expected_sorted)

    def test_sort_songs_by_last_word(self):
        """Tests sorting songs by the first letter of the last word."""
        song_titles = ["Song Title 1", "Another Song Title", "Final Song"]
        length_songs = ["2.10", "3.40", "1.20"]
        expected_sorted = [
            ("Song Title 1", "2.10"),
            ("Final Song", "1.20"),
            ("Another Song Title", "3.40"),
        ]
        sorted_songs = sort_songs(song_titles, length_songs, last_word)
        self.assertEqual(sorted_songs, expected_sorted)

    def test_sort_songs_invalid_input_length(self):
        """Tests sort_songs with unequal list lengths."""
        song_titles = ["Song 1", "Song 2"]
        length_songs = ["3.00"]  # Different length than song_titles
        self.assertIsNone(sort_songs(song_titles, length_songs, song_length))

    def test_sort_songs_invalid_input_type(self):
        """Tests sort_songs with non-string input."""
        song_titles = ["Song 1", "Song 2"]
        length_songs = [3.00, "4.15"]  # Invalid type in length_songs
        self.assertIsNone(sort_songs(song_titles, length_songs, song_length))

