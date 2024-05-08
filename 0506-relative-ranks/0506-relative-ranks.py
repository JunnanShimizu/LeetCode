class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [0] * len(score)
        
        for i in range(len(score)):
            max_index = score.index(max(score))
            if i == 0:
                answer[max_index] = "Gold Medal"
            elif i == 1:
                answer[max_index] = "Silver Medal"
            elif i == 2:
                answer[max_index] = "Bronze Medal"
            else:
                 answer[max_index] = str(i + 1)
            score[max_index] = -1
            
        return answer