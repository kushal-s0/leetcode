class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2_map = {string: j for j, string in enumerate(list2)}
        result = []
        min_sum = float('inf')
        
        for i, string in enumerate(list1):
            if string in list2_map:
                j = list2_map[string]
                current_sum = i + j            
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [string]         
                elif current_sum == min_sum:
                    result.append(string)
                    
        return result

            