
heap_length = 0

def _parent(i):
    return int(i/2)

def _left(i):
    return 2*i

def _right(i):
    return (2*i)+1

def max_heapify(A,i):
    left = _left(i+1) - 1
    right = _right(i+1) - 1
    maximum = i

    if left < heap_length and A[left] > A[maximum]:
        maximum = left
    if right < heap_length and A[right] > A[maximum]:
        maximum = right
    if maximum != i:
        A[maximum], A[i] = A[i], A[maximum]

        max_heapify(A,maximum)

def build_max_heap(A):
    #heap_length = len(A)
    for i in reversed(range(int(len(A)/2))):
        max_heapify(A,i)

def heapsort(A):
    global heap_length
    build_max_heap(A)
    for i in reversed(range(1,len(A))):
        A[0], A[i] = A[i], A[0]
        heap_length -= 1
        max_heapify(A,0)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    global heap_length
    if heap_length < 1:
        raise("list underflow")
    max_val = A[0]
    A[0] = A[len(A) - 1]
    heap_length -= 1
    max_heapify(A,0)

    return max_val

def heap_increase_key(A,i,key):
    if key < A[i]:
        raise Exception("key is lower than the pointing node: ", i)
    A[i] = key
    while i > 0 and A[_parent(i)] < A[i]:
        A[i], A[_parent(i)] = A[_parent(i)], A[i]
        i = _parent(i)

def max_heap_insert(A,key):
    global heap_length
    A.append(-1)
    heap_length = len(A)
    heap_increase_key(A,len(A)-1,key)


heap_list = [5,7,6,8,9]
#test def max_heapify
print(heap_list)
heap_length = len(heap_list)
max_heapify(heap_list, 0)
print(heap_list)

heap_list = [4,1,3,2,16,9,10,14,8,7]
#test
print(heap_list)
heap_length = len(heap_list)
build_max_heap(heap_list)
print(heap_list)

heap_list = [4,1,3,2,16,9,10,14,8,7]
print(heap_list)
heap_length = len(heap_list)
heapsort(heap_list)
print(heap_list)

heap_length = len(heap_list)
build_max_heap(heap_list)
print(heap_maximum(heap_list))
print(heap_extract_max(heap_list))
for i in range(heap_length):
    print(heap_list[i])

heap_list = [4,1,3,2,16,9,10,14,8,7]
heap_length = len(heap_list)
build_max_heap(heap_list)
print(heap_list)
heap_increase_key(heap_list,9,15)
print(heap_list)

heap_list = [4,1,3,2,16,9,10,14,8,7]
heap_length = len(heap_list)
build_max_heap(heap_list)
print(heap_list)
max_heap_insert(heap_list,15)
print(heap_list)
