class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        h={}
        for num in nums2:
            while st and st[-1]<num:
                h[st.pop()]=num
            st.append(num)
        return [h.get(num, -1) for num in nums1]