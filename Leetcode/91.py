# class Solution:
#     def numDecodings(self, s: str) -> int:
#         ans = 0
#         one = 1
#         two = 0
#         for i in range(len(s)):
#             ans = 0
#             current = s[i]
#             prev = s[i - 1] if i > 0 else ''
#
#             if current != '0':
#                 ans += one
#             if prev == '1' or (prev == '2' and current in '0123456'):
#                 ans += two
#
#             if ans == 0:
#                 return 0
#
#             two = one
#             one = ans
#
#         return ans


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        # Initialize: pprev, prev [res, last_char]
        pp, p = [1, str()], [1, s[0]]
        for c in s[1:]:
            cur = 0  # current accumulating num of decode
            # pp to cur: 2 digits s[i-1] + s[i]]
            if 10 <= int(p[1] + c) <= 26:  # [10, 26]
                cur += pp[0]  # connect
            # p to cur: 1 digit s[i]
            if 1 <= int(c) <= 9:  # [1, 10]
                cur += p[0]  # connect
            # move pointers
            pp = p
            p = [cur, c]

        return cur