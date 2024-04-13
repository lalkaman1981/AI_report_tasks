def maskify(text):
    """Replaces all characters except the last 4 in a string with '#'.

    Args:
      text: The string to be masked.

    Returns:
      A new string with all characters except the last 4 replaced with '#'.
    """
    if len(text) < 4:
        return text  # Handle strings less than 4 characters
    return "#" * (len(text) - 4) + text[-4:]