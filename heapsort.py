
class heap_node:
    def __init__(self, left, right, parent, value):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value

def max_heapify(A,i):
    left = A[i].left
    right = A[i].right
    maximum = i

    print(left, right, maximum)
    if left and A[left].value > A[i].value:
        maximum = left

    if right and A[right].value > A[i].value:
        maximum = right

    if maximum != i:
        temp = A[maximum]
        A[maximum] = A[i]
        A[i] = temp

        A[maximum].left = temp.left
        A[maximum].right = temp.right

        A[i].left = left
        A[i].right = right
        A[i].parent = A[maximum].parent

        A[maximum].parent = i

        max_heapify(A,maximum)

heap_list = list()
heap_list.append(heap_node(1,2,None,5))
heap_list.append(heap_node(None, None, 0,6))
heap_list.append(heap_node(None, None, 0,7))

for node in heap_list:
    print(node.value)

max_heapify(heap_list,0)

for node in heap_list:
    print(node.value)
