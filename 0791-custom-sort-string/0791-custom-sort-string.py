class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_counts = Counter(s)
        result = []
        for char in order:
            if char in char_counts:
                result.append(char * char_counts[char])
                del char_counts[char] 
        for char, count in char_counts.items():
            result.append(char * count)
            
        return "".join(result)
        