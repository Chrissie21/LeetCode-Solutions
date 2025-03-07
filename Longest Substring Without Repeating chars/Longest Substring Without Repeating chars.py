class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:  # If string is empty
            return 0
            
        # Dictionary that stores last pos of each char
        char_position = {}
        max_length = 0
        start = 0
        
        # Iterate through the string using end pointer
        for end, char in enumerate(s):
            # If duplicate found, update start pointer
            if char in char_position and char_position[char] >= start:
                start = char_position[char] + 1
            else:
                # Update max_length if current window is longer
                max_length = max(max_length, end - start + 1)
                
            # Update last position of current character
            char_position[char] = end
        
        return max_length