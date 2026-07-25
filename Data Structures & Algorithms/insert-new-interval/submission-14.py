
'''
We are given a series of intervals, sorted by starting time.
Insert a new interval s.t. there are no overlapping intervals.
Keep increasing while end_time < new start_time.
if it overlaps, merge and reanalyze. 

'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        prevSt, nxtSt =  10001, -1
        for i, interval in enumerate(intervals):
            st,ed = interval[0],interval[1]
            if newInterval[0] <= st <= newInterval[1] or newInterval[0] <= ed <= newInterval[1] or st <= newInterval[0] <= ed or st<= newInterval[1] <=ed :
                newInterval[0] = min(newInterval[0],st)
                newInterval[1] = max(newInterval[1],ed)
            else:
                res.append([st,ed])
        if len(res)==0:
            return [newInterval]
        ed = res[0][1]
        i = 0
        while i < len(res) and (ed < newInterval[0]) :
            ed = res[i][1]
            if ed >= newInterval[0]:
                break
            i+=1
        res.insert(i, newInterval)

        return res
