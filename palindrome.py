
"""
判断一个字符是否是回文串
1 快慢指针定位中间节点（这里要区分奇偶情况）
1.1 奇数情况，中点位置不需要矫正
1.2 偶数情况，使用偶数定位中点策略，要确定是返回上中位数或下中位数
1.2.1 如果是返回上中位数，后半部分串头取next
1.2.2 如果是返回下中位数，后半部分串头既是当前节点位置，但前半部分串尾要删除掉当前节点
2 从中间节点对后半部分逆序，或者将前半部分逆序
3 一次循环比较，判断是否为回文
4 恢复现场
"""

import sys

sys.path.append('singly_linked_list')
from singly_linked_list import SinglyLinkedList

def reverse(head):
    reverse_head = None
    while head:
        next = head._next
        head._next = reverse_head
        reverse_head = head
        head = next

    return reverse_head

def is_palindrome(l):
    l.print_all()
    slow = l._head
    fast = l._head
    position = 0
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        position += 1

    reverse_node = reverse(slow)
    head_node = l._head
    is_palin = True
    while (head_node and reverse_node):
        if (head_node.data == reverse_node.data):
            head_node = head_node._next
            reverse_node = reverse_node._next
        else:
            is_palin = False
            break
    return is_palin

if __name__ == '__main__':

    test_str_arr = ['ab','aa','aba','abba','abcdba']
    for str in test_str_arr:
        l = SinglyLinkedList()
        for i in str:
            l.insert_value_to_head(i)

        print(is_palindrome(l))
