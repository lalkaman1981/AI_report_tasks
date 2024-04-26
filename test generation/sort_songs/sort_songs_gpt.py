from collections.abc import Callable

def song_length(x: tuple[str]) -> float:
    """
    Function to extract the song length from a tuple.
    """
    return float(x[1])

def title_length(x: tuple[str]) -> int:
    """
    Function to calculate the length of the song title.
    """
    return len(x[0])

def last_word(x: tuple[str]) -> str:
    """
    Function to extract the last word of the song title.
    """
    return x[0].split()[-1]

def sort_songs(
    song_titles: list[str],
    length_songs: list[str],
    key_: Callable[[tuple], int | str | float]
) -> list[tuple] | None:
    """
    Function to sort songs based on the specified key.

    Args:
    - song_titles: List of song titles.
    - length_songs: List of corresponding song lengths.
    - key_: Callable function to determine the sorting key.

    Returns:
    - Sorted list of tuples containing song title and length, or None if input lists are not compatible.
    """
    # Check if input lists have the same length and are non-empty
    if len(song_titles) != len(length_songs) or len(song_titles) == 0:
        return None

    # Combine song titles and lengths into tuples
    songs = list(zip(song_titles, length_songs))

    # Sort the list of songs using the specified key function
    songs.sort(key=key_)

    return songs