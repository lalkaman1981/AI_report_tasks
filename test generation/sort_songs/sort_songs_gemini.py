from collections.abc import Callable


def song_length(x: tuple[str]) -> float:
    """
    Converts the song length string to a float and returns it.

    Args:
        x (tuple[str]): A tuple containing song title and song length.

    Returns:
        float: Song length as a float.
    """
    return float(x[1])


def title_length(x: tuple[str]) -> int:
    """
    Returns the length of the song title.

    Args:
        x (tuple[str]): A tuple containing song title and song length.

    Returns:
        int: Length of the song title.
    """
    return len(x[0])


def last_word(x: tuple[str]) -> str:
    """
    Returns the first letter of the last word in the song title.

    Args:
        x (tuple[str]): A tuple containing song title and song length.

    Returns:
        str: First letter of the last word in the song title.
    """
    return x[0].split()[-1][0]


def sort_songs(
    song_titles: list[str],
    length_songs: list[str],
    key_: Callable[[tuple], int | str | float]) -> list[tuple] | None:
    """
    Sorts songs based on the specified key.

    Args:
        song_titles (list[str]): List of song titles.
        length_songs (list[str]): Corresponding list of song lengths.
        key_ (Callable[[tuple], int | str | float]): Function that determines the sorting order.

    Returns:
        list[tuple] | None: Sorted list of tuples (song title, song length) or None if invalid input.
    """

    if len(song_titles) != len(length_songs):
        return None

    for title, length in zip(song_titles, length_songs):
        if not isinstance(title, str) or not isinstance(length, str):
            return None

    sorted_songs = list(zip(song_titles, length_songs))
    sorted_songs.sort(key=key_)
    return sorted_songs
