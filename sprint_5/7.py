def sift_down(heap, idx):
    left = 2 * idx
    right = 2 * idx + 1
    size = len(heap) - 1
    if left > size:
        return idx
    if (right <= size) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx
