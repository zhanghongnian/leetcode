# -*- coding: utf-8 -*- 

# 3. 三次反转 时间 O(n)，空间 O(1)
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2: # 边界条件，只有一个元素
            return
        k = k % l 
        if k == 0: # 边界条件，l 是 k 的倍数
            return
        
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


