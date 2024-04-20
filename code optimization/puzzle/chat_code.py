"""
Chat gpt puzzle program
"""

def validate_board_gpt(board):
    """
    validate by AI
    """
    size = len(board)

    def has_duplicates(cells):
        seen = set()
        for cell in cells:
            if cell.isdigit():
                if cell in seen:
                    return True
                seen.add(cell)
        return False

    # Check rows for duplicates
    for row in board:
        if has_duplicates(row):
            return False

    # Check columns for duplicates
    for col in range(size):
        if has_duplicates(board[row][col] for row in range(size)):
            return False

    # Check blocks for duplicates
    block_size = int(size ** 0.5)
    for i in range(0, size, block_size):
        for j in range(0, size, block_size):
            block = [board[i + m][j + n] for m in range(block_size) for n in range(block_size)]
            if has_duplicates(block):
                return False

    return True
