class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If 's' is already equal to 'goal', return True
        if s == goal:
            return True
            
        # Create a new string 'x' by taking the last character of 's' 
        # and prepending it to the rest of the string (excluding the last character)
        x = s[-1] + s[:-1]
        
        # Continue rotating 'x' until it matches the original string 's'
        while x != s:
            # Check if the current rotation equals the target string 'goal'
            if x == goal: 
                return True
            
            # Rotate 'x' by taking its last character and prepending it to the rest of the string
            x = x[-1] + x[:-1]
        
        # If we have checked all rotations and found no match, return False
        return False