from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       d = defaultdict(int)
       for n in nums:
          d[n]+=1 
       t = []
       m = max(d.values())
       flipped = defaultdict(list)

       for k1, v1 in d.items():
           flipped[v1].append(k1)

       print(flipped)
       for i in range(m, 0, -1):
          if flipped[i]:
            for n in flipped[i]:
                t.append(n)
                print(len(t))
                print(k)
                print(len(t) == k)
                if len(t) == k:
                    return t
       return t   

    

       
         
        
        
    

        