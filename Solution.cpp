#include <bits/stdc++.h>
using namespace std;

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

int main() {
    string s, goal;
    cin >> s >> goal;

    Solution sol;
    bool result = sol.rotateString(s = s, goal = goal);
    cout << ((result) ? "True" : "False") << endl;
}