# 796. Rotate String

__Type:__ Easy <br>
__Topics:__ String, String Matching <br>
__Companies:__ Google, Amazon, Meta, Wells Fargo, Apple, Adobe, Bloomberg, Microsoft, tcs, Visa, SAP <br>
__Leetcode Link:__ [Rotate String](https://leetcode.com/problems/rotate-string)
<hr>

Given two strings `s` and `goal`, return `true` _if and only if_ `s` _can become_ `goal` _after some number of __shifts__ on_ `s`.

A __shift__ on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ s = "abcde", goal = "cdeab" <br>
__Output:__ true

- __Example 2:__ <br>
__Input:__ s = "abcde", goal = "abced" <br>
__Output:__ false
<hr>

### Constraints
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.