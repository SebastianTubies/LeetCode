# There is a malfunctioning keyboard where some letter keys do not work. All 
# other keys on the keyboard work properly. 
# 
#  Given a string text of words separated by a single space (no leading or 
# trailing spaces) and a string brokenLetters of all distinct letter keys that are 
# broken, return the number of words in text you can fully type using this keyboard. 
# 
#  
#  Example 1: 
# 
#  
# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
#  
# 
#  Example 2: 
# 
#  
# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
#  
# 
#  Example 3: 
# 
#  
# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 10⁴ 
#  0 <= brokenLetters.length <= 26 
#  text consists of words separated by a single space without any leading or 
# trailing spaces. 
#  Each word only consists of lowercase English letters. 
#  brokenLetters consists of distinct lowercase English letters. 
#  
# 
#  Related Topics Hash Table String 👍 923 👎 39


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        words = text.split()
        broken = set(brokenLetters)

        writeable_words = 0

        for word in words:

            if all(letter not in broken for letter in word):

                writeable_words += 1


        return writeable_words

# leetcode submit region end(Prohibit modification and deletion)
