class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

      # This sliding window is iterating over a string to find the longest 
      # substring without repeating chars.
      # https://leetcode.com/problems/longest-substring-without-repeating-characters/
        
        left = 0 # Initialize left pointer
        maxLength = 0 # Initialize length variable to return the max lenght
        char_set = set() # Create a set to save the non-repeated characters

      # Sliding window loop
      for right in range(len(s)): 
        while s[right] in set:
          char_set.remove(s[left])
          left += 1
        set.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    return maxLength


testString = Solution("abcabcbb")
print(testString.lengthOfLongestSubstring)
