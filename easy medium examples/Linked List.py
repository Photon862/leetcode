
# reverse the list

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # prev is the new reversed list
        # curr is the set to the head of original list (the first node)
        prev, curr = None, head

        # go until curr is empty
        while curr:
            # new variable temp store the next node so temp = 2 if 1,2,3 list
            temp = curr.next
            #  override the next node head to none so it points backwards
            curr.next = prev
            # prev is now the current head
            prev = curr
            # move the current pointer  to the next node stored in temp
            curr = temp
            # the process repeats down the line

        #return reversed list
        return prev


# merge 2 lists already sorted in order

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # creates 2 variables tied to 1 node listNode()
        # dummy stays at 1st node while "node" is used to move along the list adding the items in
        # dummy is 0 a fake node at the left side before starting the list

        dummy = node = ListNode()

        # while list1 and list2 have still nodes inside
        while list1 and list2:
            # if list1 value is smaller than list2 value
            if list1.val < list2.val:
                # add list1 node to the final list
                node.next = list1
                # move list1 to next node
                list1 = list1.next
            else:
                # add list2 node to the final list
                node.next = list2
                # move list2 to next node
                list2 = list2.next
            # after finishing the if logic, move to next node for next item to be put in
            node = node.next

        # when one list is finished, add the rest of the other list to final list
        node.next = list1 or list2

        # return the merged list skipping the fake 0 at the start
        # if return dummy its eg 0,1,2,3
        # return dummy.next is 1,2,3
        # return node = last node so jsut 3 since we moved it to the end
        return dummy.next


# rearrange a linked list nodes to a fixed combination

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 pointers 1 slow and 1 fast to find middle of the list
        slow, fast = head, head.next

        # while fast pointer and the next of fast pointer exist - stops when it hits end
        while fast and fast.next:
            # move slow by 1 step
            slow = slow.next
            # move fast by 2 steps
            fast = fast.next.next
            # this will find the middle because slow is always half speed of fast

        # new variable second is node after slow (middle)
        second = slow.next
        # cut the list in half by setting slow next to None
        prev = slow.next = None

        # reverse the second half of the list
        while second:
            # temp variable to store next node
            tmp = second.next
            # set the next node to be other direction = none
            second.next = prev
            # move prev node back to current "second" node
            prev = second
            # move "second" node to the next node stored as tmp
            second = tmp

        # pointers for 1st and 2nd half of list - 2nd half is already reversed
        first, second = head, prev

        # while 2nd is not empty
        while second:
            # temp varaibles to store next nodes in each list
            tmp1, tmp2 = first.next, second.next
            # link first node to "second" node
            first.next = second
            # link "second" node to the next node in first half stored in tmp1
            second.next = tmp1
            # move the pointers forward to the next nodes
            first, second = tmp1, tmp2
            # the loop repeats