# 퀵 소트(Quick Sort) - 로무토 파티션
* 피벗을 기준으로 좌우를 나누는 분할정복 알고리즘

```python
def quicksort(A, lo, hi):
  def partition(lo, hi):
    pivot = A[hi] # 맨 오른쪽을 피벗(기준)
    left = lo
    for right in range(lo,hi):
      if A[right] < pivot:
        A[left], A[right] = A[right], A[left]
        left +=1
    
   A[left], A[hi] = A[hi], A[left]
   return left
   
  if lo < hi:
    pivot = partition(lo, hi)
    quicksort(A, lo, pivot-1)
    quicksort(A, pivot+1, hi)
    
    
# 맨 왼쪽 피벗 기준 쉬운 버전
def quickSort(x):
    n = len(x)
    if n <= 1: return x
    
    pivot = x[0]
    left = []
    right = []

    for i in range(1,n):
        if x[i] < pivot:
            left.append(x[i])
        else:
            right.append(x[i])
            
    return quickSort(left) + [pivot] + quickSort(right)   # 리스트를 이어 붙인다.
```

- 매우 효율적인 알고리즘이나 최악의 경우 O(n**2)
- 입력값에 따라 성능 차이가 심함
