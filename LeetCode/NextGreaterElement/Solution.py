class Solution(object):
    @staticmethod
    def nextGreaterElement(nums1, nums2):
        n = len(nums1)
        out = [-1]*n
        
        next_greater = {}
        temp = []
        for x in nums2:
            while temp and temp[-1] < x:
                next_greater[temp.pop()] = x
            temp.append(x)

        for i in range(n):
            if nums1[i] in next_greater:
                out[i] = next_greater[nums1[i]]
        return out

a=Solution.nextGreaterElement([4,1,2], [1,3,4,2])
print(a, a == [-1,3,-1])
b=Solution.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
print(b, b == [7,7,7,7,7])
