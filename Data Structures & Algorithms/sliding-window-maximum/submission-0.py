class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices in decreasing order of values
        q = deque()

        # Final answer
        result = []

        for right in range(len(nums)):

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index
            q.append(right)

            # Remove indices that are outside the window
            if q[0] < right - k + 1:
                q.popleft()

            # Window is fully formed
            if right >= k - 1:
                result.append(nums[q[0]])

        return result