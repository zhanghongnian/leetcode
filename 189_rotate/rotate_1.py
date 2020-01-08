# -*- coding: utf-8 -*- 

# 1. 求出应该交换的下标，逐个交换，时间 O(n)，空间 O(1)
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        if k == 0: # 边界条件，不需要处理
            return
        count = 0 # 计数器，完成 l 次交换后，结束
        cur, nxt, tmp, tmp2 = 0, 0, 0, 0
        for i in range(k):
            cur = i # 当前指针
            tmp = nums[cur]
            while True:
                nxt = (cur+k) % l # 下一次的指针 
                nums[nxt], tmp = tmp, nums[nxt] 
                # print(count, nums)
                cur = nxt
                count += 1
                if i == nxt: # 循环结束
                    break
            if count >= l:
                return

