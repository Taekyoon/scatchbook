
class _Node:
    def __init__(self, e):
        self.element = e
        self.next = None

    def setNext(self, n):
        self.next = n

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def frontAdd(self, d):
        new_node = _Node(d)
        if self.size is 0:
            self.head = new_node
            new_node.setNext(None)
        else:
            new_node.setNext(self.head)
            self.head = new_node

        self.size += 1

    def backAdd(self, d):
        new_node = _Node(d)
        new_node.setNext(None)

        if self.size is 0:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next

            cur_node.setNext(new_node)

        self.size += 1

    def frontDel(self):
        if self.size is 1:
            self.head = None
        else:
            del_node = self.head
            self.head = del_node.next

        self.size -= 1

    def backDel(self):
        if self.size is 1:
            self.head = None
        elif self.size is 2:
            self.head = self.head.next
        else:
            cur_node = self.head
            while cur_node.next.next is not None:
                cur_node = cur_node.next
            cur_node.setNext(None)

        self.size -= 1

    def printList(self):
        if self.size is 0:
            print('no node')
            return

        cur_node = self.head
        ret = cur_node.element + '->'
        while cur_node.next is not None:
            cur_node = cur_node.next
            ret += cur_node.element + '->'

        ret += 'end'
        print(ret)


list = LinkedList()

list.frontAdd('c')
list.frontAdd('b')
list.frontAdd('a')

list.printList()
print(list.size)

list.backAdd('d')
list.backAdd('e')
list.backAdd('f')

list.printList()
print(list.size)

list.frontDel()
list.frontDel()
list.frontDel()

list.printList()
print(list.size)

list.backDel()
list.backDel()
list.backDel()

list.printList()
print(list.size)
