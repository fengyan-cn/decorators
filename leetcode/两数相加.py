class Solution(object):
    def addTwonumbers(self, ListNode1, ListNode2):
        pass

unit1 = ListNode1 % 100 % 10
decade1 = ListNode1 % 100 - unit1
hundred1 = List1Node1 - unit1 - decade1
unit2 = ListNode2 % 100 % 10
decade2 = ListNode2 % 100 - unit2
hundred2 = List1Node2 - unit1 - decade2
print()