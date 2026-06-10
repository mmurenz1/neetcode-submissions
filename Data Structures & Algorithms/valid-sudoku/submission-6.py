class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)

        cols = defaultdict(set)

        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                box = (r // 3, c // 3)

                if (
                    value in rows[r] or
                    value in cols[c] or
                    value in boxes[box]
                ):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True