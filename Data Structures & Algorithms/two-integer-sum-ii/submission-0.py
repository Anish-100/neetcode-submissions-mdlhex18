class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end:
            result = numbers[start] + numbers[end]
            print(start,end, result)
            if result == target:
                return [start+1,end+1]
            if result < target:
                start+=1
            if result > target:
                end-=1