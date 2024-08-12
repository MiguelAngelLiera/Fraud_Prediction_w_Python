class Solution():
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        t=0
        for j in range(n):
            for i in range(m):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                elif nums1[i] > nums2[j]:
                    t=nums1[i]
                    nums1[i] = nums2[j]
                    self.recorrer(nums1,t,i)
                

    def recorrer(self,arr,t,i):
        print(type(arr))
        print(len(arr))
        for k in range(i+1, len(arr)):
            f = arr[k]
            arr[k] = t
            t = f