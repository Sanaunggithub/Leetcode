public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        return mergeSort(head);
    }

    public ListNode mergeSort(ListNode head){

        if(head == null || head.next == null) return head;

        ListNode mid = getMiddle(head);
        ListNode right = mid.next;
        mid.next = null ; // cut the list

        ListNode left_sorted = mergeSort(head);
        ListNode right_sorted = mergeSort(right);

        return merge(left_sorted, right_sorted);
    }

    public ListNode getMiddle(ListNode head){
        ListNode slow = head, fast = head, prev = null;
        while(fast != null && fast.next != null) {
            prev = slow; // remember node before slow
            slow = slow.next;
            fast = fast.next.next;
        }
        return prev;
    }

    public ListNode merge(ListNode left, ListNode right){
        ListNode l = left;
        ListNode r = right;
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while(l != null && r != null){
            if(l.val <= r.val){
                current.next = l;
                l = l.next;
            }
            else {
                current.next = r;
                r = r.next;
            }
            current = current.next;
        }

        if(l != null) current.next = l;
        if(r != null) current.next = r;

        return dummy.next;
    }
}
