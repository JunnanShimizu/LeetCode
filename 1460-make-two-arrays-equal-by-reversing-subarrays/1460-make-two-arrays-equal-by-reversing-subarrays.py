class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_count = {}
        arr_count = {}
        
        for i in range(len(target)):
            t_val = target[i]
            a_val = arr[i]
            target_count[t_val] = target_count.get(t_val, 0) + 1
            arr_count[a_val] = arr_count.get(a_val, 0) + 1
            
        if target_count == arr_count:
            return True
        else:
            return False