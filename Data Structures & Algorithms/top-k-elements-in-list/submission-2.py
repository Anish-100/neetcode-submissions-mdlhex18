class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        freq_list= [[] for x in range(len(nums))]
        final_list = []
        for i in nums:
            if i in num_dict:
                num_dict[i]+=1
            else:
                num_dict[i]=1
        for key,val in num_dict.items():
            freq_list[val-1].append(key)
        print('N-dict',num_dict)
        print('F-list',freq_list)
        i=len(nums)-1
        counter=0
        while counter < k:
            if freq_list[i] != []:
                final_list.extend(freq_list[i])
                counter=len(final_list)
            i-=1
        return final_list
        
        