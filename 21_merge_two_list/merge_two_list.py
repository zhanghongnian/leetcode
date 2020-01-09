# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None # 头指针
        tail = None # 尾指针

        while True:
            # 判断是否满足推出条件
            if l1 is None and l2 is None:
                break
            # 对比两个链表当前指针值
            tmp = 0
            moveL1 = False
            moveL2 = False
            if l2 is None:
                tmp = l1.val
                moveL1 = True
            elif l1 is None:
                tmp = l2.val
                moveL2 = True
            elif l1.val < l2.val:
                tmp = l1.val
                moveL1 = True
            else:
                tmp = l2.val
                moveL2 = True
            node = ListNode(tmp)
            if head is None:
                # 给头指针赋值
                head = node
                tail = head
            else:
                tail.next = node
                tail = tail.next
            # 向后移动下标
            if moveL1:
                l1 = l1.next
            if moveL2:
                l2 = l2.next
        return head

