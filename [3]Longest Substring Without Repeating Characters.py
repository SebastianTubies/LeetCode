# Given a string s, find the length of the longest substring without duplicate 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
# 
#  Related Topics Hash Table String Sliding Window 👍 43085 👎 2108


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0

        char_set = set()
        max_length = 0
        start = 0

        for end in range(len(s)):

            while s[end] in char_set:

                char_set.remove(s[start])
                start += 1

            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)

        return max_length
        
# leetcode submit region end(Prohibit modification and deletion)
