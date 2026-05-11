class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_length = 0
        seen = set()

        while right < len(s):
            if s[right] in seen:
                left = right = left + 1
                seen.clear()
            else:
                seen.add(s[right])
                right += 1
            max_length = max(max_length, len(seen))

        return max_length
