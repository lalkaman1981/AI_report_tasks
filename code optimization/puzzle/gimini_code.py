"""
Chat gemini puzzle program
"""

def validate_board_gemini(board: list) -> bool:
  """
  Checks if a given board is valid for a logic puzzle game.

  Args:
      board (list): A list of strings representing the game board.

  Returns:
      bool: True if the board is valid, False otherwise.
  """

  board_size = len(board)

  # Combine row and column checks with early exit
  for row in board:
    unique_numbers = set()
    for char in row:
      if char not in " *":
        if char in unique_numbers:
          return False
        unique_numbers.add(char)

  for col in range(board_size):
    unique_numbers = set()
    for row in range(board_size):
      char = board[row][col]
      if char not in " *":
        if char in unique_numbers:
          return False
        unique_numbers.add(char)

  # Sub-grid check with early exit (optimized loop)
  for row_start in range(0, board_size, 3):
    for col_start in range(0, board_size, 3):
      unique_numbers = set()
      for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
          char = board[row][col]
          if char not in " *":
            if char in unique_numbers:
              return False
            unique_numbers.add(char)

  return True