class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths of 's' and 'goal' are different
        # If they are, 'goal' cannot be a rotation of 's'
        if len(s) != len(goal):
            return False
        
        # Create a new string by concatenating 's' with itself
        double_string = s + s
        
        # Check if 'goal' is a substring of 'double_string'
        # If it is, return True; otherwise, return False
        return double_string.find(goal) != -1