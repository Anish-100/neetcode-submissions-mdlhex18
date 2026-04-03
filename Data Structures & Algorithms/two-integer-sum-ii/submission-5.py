class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end= 0,len(numbers)-1

        while start < end:
            result = (numbers[start] + numbers[end])
            if result < target:
                start+=1
            elif result > target:
                end-=1
            else:
                return [start+1,end+1]