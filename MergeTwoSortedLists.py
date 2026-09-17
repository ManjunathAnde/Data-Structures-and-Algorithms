class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        resultant = ListNode(0) #Creating a resultant list with fake starting node (that we disregard later)
        curr = resultant #pointer to move through the resultant linked list
        while list1 and list2: #Stop the loop when one list runs out of nodes
            if list1.val<list2.val: #if node1 in list1 is smaller than node1 in list2, add list1 node1 to resultant
                curr.next=list1 
                list1=list1.next #then move to next node in list1
                curr=curr.next #also move the curr pointer to make sure next coming number is held in right place
            elif list1.val>list2.val:
                curr.next=list2
                list2=list2.next
                curr=curr.next 
            elif list1.val==list2.val: #if both are same, we can add either one (list.val or list2.val)
                curr.next=list2
                list2=list2.next
                curr=curr.next 
        curr.next = list1 or list2 #When one list runs out, we can directly add remaining nodes of other list to resultant
        return resultant.next #because both nodes are already sorted
    #then return resultant.next disregarding the "0" node used as initialization help
	

	
	

        