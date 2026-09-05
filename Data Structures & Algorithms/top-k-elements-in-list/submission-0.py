

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
  
        for num in nums:
            if(num in hash_map):
                hash_map[num] += 1
            else:
                hash_map[num] = 1   


     
        freq_list = []
        for num in hash_map:
            count = hash_map[num]
       
            freq_list.append((count,num))

       
        freq_list.sort(reverse=True)

        res = []
        for i in range(k):
           
            count, number = freq_list[i]
            res.append(number)

        return res





        