class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = []
        
        for n in str(num):
            num_arr.append(n)
        
        max_found = False
        first = -1
        for i in range(len(num_arr)):
            cur_max = -1
            max_i = i
            for i2 in range(len(num_arr) - 1, i, -1):
                if num_arr[i] < num_arr[i2] and int(num_arr[i2]) > cur_max:
                    max_found = True
                    cur_max = int(num_arr[i2])
                    max_i = i2
            if max_found:
                first = i
                break
        
        temp = num_arr[first]
        num_arr[first] = num_arr[max_i]
        num_arr[max_i] = temp
        
        res = ""
        for n in num_arr:
            res += n
            
        return int(res)
                    
        
                
                
            
                    
                
            