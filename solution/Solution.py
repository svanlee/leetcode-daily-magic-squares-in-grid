# Solution in PY
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        row = len(grid)
        column = len(grid[0])
        
        # Initialize a variable to store the count of magic squares
        ans = 0
        
        # Iterate over all possible 3x3 sub-grids in the grid
        for i in range(0, row - 2):  
            for j in range(0, column - 2):  
                # Check if the current 3x3 sub-grid contains all numbers from 1 to 9
                if {grid[i+k][j+l] for k in range(3) for l in range(3)} != {i for i in range(1, 10)}:
                    # If not, skip to the next sub-grid
                    continue
                
                # Initialize a flag to indicate whether the current sub-grid is a magic square
                okay = True
                
                # Calculate the sum of the first row of the sub-grid
                sm = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                
                # Check if the sum of the diagonal elements is equal to the sum of the first row
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != sm:
                    # If not, skip to the next sub-grid
                    continue
                
                # Check if the sum of the anti-diagonal elements is equal to the sum of the first row
                if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != sm:
                    # If not, skip to the next sub-grid
                    continue
                
                # Check if the sum of each row and each column is equal to the sum of the first row
                for k in range(3):
                    temp = 0
                    # Calculate the sum of the k-th row
                    for l in range(3):
                        temp += grid[i + k][j + l]  
                    if  temp != sm:
                        # If the sum of the k-th row is not equal to the sum of the first row, set the flag to False
                        okay = False
                        break
                    
                    temp = 0
                    # Calculate the sum of the k-th column
                    for l in range(3):
                        temp += grid[i + l][j + k]  
                    if  temp != sm:
                        # If the sum of the k-th column is not equal to the sum of the first row, set the flag to False
                        okay = False
                        break
                
                # If the flag is still True, it means the current sub-grid is a magic square, so increment the count
                if okay:
                    ans += 1
        
        # Return the count of magic squares
        return ans