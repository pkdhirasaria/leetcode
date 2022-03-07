/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *slow=head, *fast=head, *temp;
	for(int count = 1; count<=n; count++)
		fast = fast->next;
	while(fast != NULL){
	temp = slow;
	slow= slow->next;
	fast=fast->next;
	}
    
	if (slow==head)
				head=head->next;

	else{
	temp->next = slow->next;
	slow->next = NULL;
}


	return head;

    }
};