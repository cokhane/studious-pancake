'''

start: 020426

start again: 081826

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        print(f"{list1}")
        print(f"{list2}")

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6

        head = node1

        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

        return True

    @staticmethod
    def merge_sort_repeating_zero(list1, list2):
        print('merge_sort!!!: ')
        new_list = list1 + list2
        i = 0
        restart = 0
        ''' merge sort '''
        while i < len(new_list):
            if i + 1 < len(new_list):
                print(f"before: {new_list[i]}")
                print(f"before: {new_list[i+1]}")
                if new_list[i] > new_list[i+1]:
                    new_list[i],new_list[i+1] = new_list[i+1], new_list[i]
                    print(f"latest: ",new_list)
                    i = 0
            i+=1
        print(new_list)
        return True


    @staticmethod
    def merge_sort_no_repeating(list1, list2):
        print('merge_sort!!!: ')
        new_list = list1 + list2

        for i in new_list:
            print('-----')
            for j in new_list:
                print('print i: ',i)
                print(j)

axe = Solution()
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)

head1 = node1

head2 = node4

if __name__ == '__main__':
    # print(axe.mergeTwoLists(head1,head2))
    print(axe.merge_sort_no_repeating([1,4,3],[6,5,2]))