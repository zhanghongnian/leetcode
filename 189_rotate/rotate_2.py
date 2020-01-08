# -*- coding: utf-8 -*- 

# 2. 每次右移一位，右移n次，时间 O(n^2)，空间 O(1) -- (超时)
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
        for i in range(k):
            self.rotate_once(nums, l)
    
    def rotate_once(self, nums, l):
        tmp = nums[l-1]
        for i in range(l-1):
            nums[l-i-1] = nums[l-i-2]
        nums[0] = tmp

