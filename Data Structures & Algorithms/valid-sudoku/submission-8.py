class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        use a hashset to check for duplicates
        for rows and columns its pretty simple, just add to the hashset during each iteraiton if not already in the hashset
        for the squares, use the equation r // 3, c // 3 as the key for the hashmap. because that will alwyas give you the INDEX of whatveer square you want. from there, check within the square. each square is a key in the hashmap
        """



        rows = defaultdict(set) #use hashset to check for duplicates
        cols = defaultdict(set) #col is the key
        squares = defaultdict(set) # key is a pair: (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #skip if empty
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]: #use a tuple of pairs in squares to access the values
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c]) # r // 3, c // 3 is basically telling us the index of the square that this belongs to
        return True