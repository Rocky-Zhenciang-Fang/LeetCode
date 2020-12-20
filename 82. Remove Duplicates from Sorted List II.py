from DS import ListNode
import DS


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)  # construct a dummy node
        dummy.next = head

        pre = dummy  # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                # this will be verified by next line
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3, 3, 4, 4, 5, 5]
    head = DS.arr2LinkedNode(arr)
    head = sol.deleteDuplicates(head)
    DS.print_ListNode(head)
