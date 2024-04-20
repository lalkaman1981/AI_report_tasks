"""
fixing old problems
"""

import matplotlib.pyplot as plt
from time import time
from memory_profiler import profile

# @profile
def validate_board_mine(board:list)->bool:
    """"
    list->bool
    Checks a list with puzzle game and
    says if it is correct
    """
    for line in board:
        lst=[]
        for symb in line:
            if symb!=' ' and symb!="*":
                if symb in lst:
                    return False
                else:
                    lst.append(symb)
    for ind in range(len(board)):
        lst0=[]
        for line1 in board:
            if line1[ind]!=' ' and line1[ind]!="*":
                if line1[ind] not in lst0:
                    lst0.append(line1[ind])
                else:
                    return False
    k=len(board)
    for chislo in range(len(board)):
        lst007=[]
        sum1=0
        for line001 in board:
            if line001[chislo]!=' ' and line001[chislo]!='*' and k-1>sum1:
                if line001[chislo] in lst007:
                    return False
                lst007.append(line001[chislo])
            elif k-1==sum1:
                for g in line001[len(board)-k:]:
                    if g!=' ' and g!='*':
                        if g in lst007:
                            return False
                        lst007.append(g)
            sum1+=1
        k-=1
    return True

# @profile
def validate_board_gpt(board):
    """
    Check if the puzzle game board is valid.

    Args:
        board (list): List of strings representing the game board.

    Returns:
        bool: True if the board is valid, False otherwise.
    """

    seen_rows = [set() for _ in range(9)]
    seen_cols = [set() for _ in range(9)]
    seen_blocks = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != ' ' and board[i][j] != '*':
                digit = board[i][j]

                # Check row
                if digit in seen_rows[i]:
                    return False
                seen_rows[i].add(digit)

                # Check column
                if digit in seen_cols[j]:
                    return False
                seen_cols[j].add(digit)

                # Check block
                block_index = 3 * (i // 3) + j // 3
                if digit in seen_blocks[block_index]:
                    return False
                seen_blocks[block_index].add(digit)

    return True

# @profile
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


if __name__ == "__main__":

    lst_time1 = []
    lst_frequency1 = []
    lst_time2 = []
    lst_frequency2 = []

    board = ["**** ****",
            "***1 ****",
            "**  3****",
            "* 4 7****",
            "     9 5 ",
            " 6  83  *",
            "3   1  **",
            "  8  2***",
            "  2  ****"]

    for i in range(0, 5000, 50):

        start = time()
        for _ in range(i):
            validate_board_mine(board)
        stop = time() - start

        lst_time1.append(stop)
        lst_frequency1.append(i)

        start = time()
        for _ in range(i):
            validate_board_gpt(board)
        stop = time() - start

        #if you want to check gemini:
        # start = time()
        # for _ in range(i):
        #     validate_board_gemini(board)
        # stop = time() - start

        lst_time2.append(stop)
        lst_frequency2.append(i)


    plt.plot(lst_frequency1, lst_time1, label='old by me', marker='o')
    plt.plot(lst_frequency2, lst_time2, label='new by AI', marker='o')

    plt.xlabel('frequency')
    plt.ylabel('Time')

    plt.legend()

    plt.show()
