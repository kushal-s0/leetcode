class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        l=0
        r=0
        count=0
        while l<len(seats):
            count+=abs(seats[l]-students[r])
            l+=1
            r+=1
        return count
        