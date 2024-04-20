"""
Chat gpt puzzle program
"""

def validate_board_gpt(board: list) -> bool:
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
