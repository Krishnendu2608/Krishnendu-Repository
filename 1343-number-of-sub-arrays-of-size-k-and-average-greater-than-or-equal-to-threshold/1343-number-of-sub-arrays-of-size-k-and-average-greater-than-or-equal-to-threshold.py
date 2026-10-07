class Solution(object):
    def numOfSubarrays(self, arr, k, th):
        current_sum=sum(arr[0:k])
        count=0
        if (current_sum)/k>=th:
            count+=1
        for i in range(0,len(arr)-k):
            current_sum-=arr[i]
            current_sum+=arr[i+k]
            avg=(current_sum)/k
            if avg>=th:
                count+=1
        return count