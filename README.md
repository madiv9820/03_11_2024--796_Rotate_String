# Approaches to Determine if One String is a Rotation of Another
- ## Approach 1:- Brute Force using Rotation

    - ### Intuition
        - The goal is to determine if the string `goal` can be obtained by rotating the string `s`. A rotation of a string involves moving characters from one end to the other. For example, rotating "abcde" can yield "eabcd", "deabc", and so forth. The task is to check all possible rotations of `s` to see if any match `goal`.

    - ### Approach
        1. **Initial Check**: First, check if `s` is already equal to `goal`. If they are the same, return `true` immediately.
        2. **Construct Initial Rotation**: Create the first rotation of `s` by taking the last character and appending the substring from the beginning to the second-to-last character.
        3. **Iterate Through Rotations**: Use a loop to rotate the string `x` until it either matches `s` again (completing a full cycle of rotations) or finds a match with `goal`. In each iteration, perform the rotation by moving the last character to the front.
        4. **Final Check**: If a match with `goal` is found during the rotations, return `true`. If all rotations are exhausted without finding a match, return `false`.

    - ### Time Complexity
        - **O(n²)**: In the worst case, where `s` is not equal to `goal`, the algorithm checks at most `n` rotations of the string `s` (where `n` is the length of the string). Each rotation involves creating a new string that takes O(n) time due to string slicing. Thus, the overall time complexity is O(n²).

    - ### Space Complexity
        - **O(n)**: The algorithm uses additional space to store the rotated string `x`. Each rotation creates a new string that can be up to the length of `s`. Therefore, the space complexity is O(n).

    - ### Code 
        ```python3 []
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
        ```
        ```C++ []
        class Solution {
            public:
                bool rotateString(string s, string goal) {
                    // If 's' is already equal to 'goal', return true
                    if(s == goal)
                        return true;
                    
                    int n = s.size(); // Get the length of the string 's'

                    // Create a new string 'x' by taking the last character of 's' 
                    // and prepending it to the rest of the string (excluding the last character)
                    string x = s.substr(n-1) + s.substr(0, n-1);

                    // Continue rotating 'x' until it matches the original string 's'
                    while(x != s) {
                        // Check if the current rotation equals the target string 'goal'
                        if(x == goal)
                            return true;

                        // Rotate 'x' by taking its last character and prepending it to the rest of the string
                        x = x.substr(n-1) + x.substr(0, n-1);
                    }

                    // If we have checked all rotations and found no match, return false
                    return false;
                }
        };
        ```

- ## Approach 2:- Concatenation Check

    - ### Intuition
        - The problem is to determine if the string `goal` can be obtained by rotating the string `s`. A rotation involves moving characters from one end of the string to the other. By concatenating `s` with itself, we can easily check if `goal` exists as a substring within this new string, which would imply that `goal` is a rotation of `s`.

    - ### Approach
        1. **Length Check**: First, verify if the lengths of `s` and `goal` are the same. If they differ, return `false`, as `goal` cannot be a rotation of `s`.
        2. **Create Double String**: Concatenate `s` with itself to create `double_string`. This string contains all possible rotations of `s`.
        3. **Substring Search**: Use the `find()` method to check if `goal` is a substring of `double_string`. If found, it indicates that `goal` is indeed a rotation of `s`.

    - ### Time Complexity
        - **O(n)**: The algorithm primarily involves checking if `goal` is a substring of `double_string`. The `find()` method runs in linear time, where `n` is the length of the strings.

    - ### Space Complexity
        - **O(n)**: The space complexity is determined by the storage of `double_string`, which is twice the length of `s`. 

    - ### Code
        ```python3 []
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
        ```
        ```C++ []
        class Solution {
            public:
                bool rotateString(string s, string goal) {
                    // Check if the lengths of 's' and 'goal' are different
                    // If they are, 'goal' cannot be a rotation of 's'
                    if (s.length() != goal.length())
                        return false;
                    
                    // Create a new string by concatenating 's' with itself
                    string double_string = s + s;
                    
                    // Check if 'goal' is a substring of 'double_string'
                    // Using find() returns the index of 'goal' in 'double_string' if found,
                    // and the condition checks if the index is valid (less than the length of double_string)
                    return double_string.find(goal) < double_string.length();
                }
        };
        ```