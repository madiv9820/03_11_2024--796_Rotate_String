#include <bits/stdc++.h>
using namespace std;

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

int main() {
    string s, goal;
    cin >> s >> goal;

    Solution sol;
    bool result = sol.rotateString(s = s, goal = goal);
    cout << ((result) ? "True" : "False") << endl;
}