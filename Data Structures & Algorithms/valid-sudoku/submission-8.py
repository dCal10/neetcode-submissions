class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create 3 hassets of lists for rows, columns, list
        size = 9
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        squares = [set() for _ in range(size)]
            
        # for i, j in sudoku
        for i, row in enumerate(board):
            for j, item in enumerate(row):
            # if digit exist
             if item != ".":
                # store digit
                digit = int(item)
                sq_index = (i // 3) * 3 + (j // 3)
                # if i, j , sqaure exist return false else add to set
                if digit in rows[i] or digit in cols[j] or digit in squares[sq_index]:
                    return False
                else:
                    rows[i].add(digit)
                    cols[j].add(digit)
                    squares[sq_index].add(digit)
        return True

           
            
           
        # return true