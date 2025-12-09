# ------------------------------------------------------------
# Add Two Numbers Using Linked Lists
# (Problem Description + Explanation + Full Code)
# ------------------------------------------------------------

# Problem Description:
# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order.
# Each node contains a single digit.
#
# Your task: Add the two numbers and return the result as a
# linked list (also in reverse order).
#
# You may assume:
# - No leading zeros exist except the number 0 itself.
#
# Example 1:
# l1 = [2,4,3], l2 = [5,6,4]
# 342 + 465 = 807 → Output: [7,0,8]
#
# Example 2:
# l1 = [0], l2 = [0] → Output: [0]
#
# Example 3:
# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# ------------------------------------------------------------
# Algorithm Explanation:
#
# We simulate normal addition the same way we add numbers by hand.
#
# Steps:
# 1. Create a dummy head node to build the result list.
# 2. Use a pointer `temp` to append new digits.
# 3. Maintain a `carry` for sums ≥ 10.
# 4. Loop while there are digits in l1, l2, or carry:
#       - Extract values (0 if node doesn't exist)
#       - Compute total = a + b + carry
#       - New digit = total % 10
#       - Update carry = total // 10
#       - Append new node with digit
#
# Time Complexity: O(max(len(l1), len(l2)))
# Space Complexity: O(max(len(l1), len(l2)))
#
# ------------------------------------------------------------

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a + b + carry
            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ------------------------------------------------------------
# MAIN (for testing in VS Code)
# ------------------------------------------------------------
# This converts Python lists → linked lists and back,
# so you can manually test the program.

def list_to_ll(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def ll_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    print("Enter first linked list digits (space separated):")
    l1 = list_to_ll(list(map(int, input().split())))

    print("Enter second linked list digits (space separated):")
    l2 = list_to_ll(list(map(int, input().split())))

    solver = Solution()
    ans = solver.addTwoNumbers(l1, l2)

    print("Output Linked List:", ll_to_list(ans))


if __name__ == "__main__":
    main()
