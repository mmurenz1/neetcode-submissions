class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}

        window_count = {}

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}

        window_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if s1_count == window_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            window_count[s2[left]] -= 1

            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            left += 1

            if s1_count == window_count:
                return True

        return False