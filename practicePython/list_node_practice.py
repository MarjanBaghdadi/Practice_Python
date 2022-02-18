from ListNode import Node, LinkedList, DoublyLinkedList

test = LinkedList()
print(test)

test.add_node(1)
test.add_node(2)
test.add_node(3)
test.add_node(4)
test.add_node(5)

test.add_multiple_nodes([6,7,8,9,10])

test.add_node_as_head(0)


print(test)
print(len(test))
print(test.values)

print("reverse: ", test.reverse())
print("reverse: ", test)

test2 = DoublyLinkedList(test)
print(test2)


