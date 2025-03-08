class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If numRows is 1 or greater than string length, return original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create list of strings for each row
        rows = [''] * numRows
        current_row = 0
        step = 1  # 1 for moving down, -1 for moving up
        
        # Traverse the string and place characters in appropriate rows
        for char in s:
            rows[current_row] += char
            
            # Change direction when we reach top or bottom
            if current_row == 0:
                step = 1  # Start moving down
            elif current_row == numRows - 1:
                step = -1  # Start moving up
            
            current_row += step
        
        # Combine all rows into final string
        return ''.join(rows)
    
# Test
if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.convert("PAYPALISHIRING", 3))  
    print(solution.convert("PAYPALISHIRING", 4))  
    print(solution.convert("A", 1))             