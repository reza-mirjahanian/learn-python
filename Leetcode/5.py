class Solution:

    # manacher's algorithm being applicable for only odd length strings,
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        s = '#' + '#'.join(s) + '#'  # s==#b#a#b#a#d#

        dp = [0 for _ in range(len(s))]  # [expression for item in iterable if condition == True]  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        center = 0
        right = 0
        for i in range(len(s)):
            print('-' * 12)
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')
            print(dp)
        return max_str


test = Solution()
print(test.longestPalindrome("babad"))

# Preprocessing the String:
# To handle even-length palindromes, the algorithm preprocesses the input string by inserting special characters (
# usually '#' symbols) between every pair of characters and at the beginning and end of the string.
# For example, the string "aba" would be transformed into "#a#b#a#".
