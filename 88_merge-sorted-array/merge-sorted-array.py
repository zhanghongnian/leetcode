# -*- coding: utf-8 -*-

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = []
        i = 0
        j = 0
        while True:
            if i == m: 
                l.extend(nums2[j:n])
                break
            if j == n:
                l.extend(nums1[i:m])
                break
            if nums1[i] <= nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1
        for z, item in enumerate(l):
            nums1[z] = item
        return
        
        