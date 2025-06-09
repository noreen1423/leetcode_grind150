class Solution:
  def topKFrequent(self, nums, k):
    #Create a dict whose key is num and value is freq of the number
    count = {}
    #Create a frequency bucket (list of lists)
    freq = [[] for i in range(len(nums)+1)] #list comprehension

    #Start adding keys-values in the dict 
    for num in nums:
      count[num]=1+count.get(num,0) #This is the key

    #cnt is a bucket in bucket list
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
