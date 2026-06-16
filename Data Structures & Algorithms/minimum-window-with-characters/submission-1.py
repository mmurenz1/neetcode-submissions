class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        need_count = len(need)

        have_count = 0

        result = [float("inf"), 0, 0]

        left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have_count += 1

            while have_count == need_count:
                if (right - left + 1) < result[0]:
                    result = [right - left + 1, left, right]
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have_count -= 1

                left += 1

        if result[0] == float("inf"):
            return ""

        return s[result[1]:result[2] + 1]
                    
