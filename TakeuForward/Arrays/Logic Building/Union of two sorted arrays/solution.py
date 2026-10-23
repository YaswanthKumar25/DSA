class Solution:
    def unionArray(self, nums1, nums2):
        i=0
        j=0
        union=[]
        while i <len(nums1) and j <len(nums2):
            if nums1[i]<=nums2[j]:
                if nums1[i] not in union:
                    union.append(nums1[i])
                i+=1
            else:
                if nums2[j] not in union:
                    union.append(nums2[j])
                j+=1
        while i <len(nums1):
            if nums1[i] not in union:
                union.append(nums1[i])
            i+=1
        while j <len(nums2):
            if nums2[j] not in union:
                    union.append(nums2[j])
            j+=1
        return union

            