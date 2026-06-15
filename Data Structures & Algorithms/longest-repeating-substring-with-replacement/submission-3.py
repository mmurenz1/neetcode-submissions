class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        left = 0

        max_freq = 0

        longest = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            window_size = right - left + 1

            while window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            longest = max(longest, window_size)

        return longest