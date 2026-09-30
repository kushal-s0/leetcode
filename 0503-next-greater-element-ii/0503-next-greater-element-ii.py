class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        ans = [-1] * len(nums)
        st = []
        for i in range((2 * len(nums)) - 1, -1, -1):
            current_val = nums[i % len(nums)]
            while len(st) != 0 and st[-1] <= current_val:
                st.pop()             
            if i < len(nums):
                if len(st) != 0:
                    ans[i] = st[-1]
                    
            st.append(current_val)

        return ans