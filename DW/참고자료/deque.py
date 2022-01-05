# Deque(데크)
# 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우,
# 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 반면,
# 데크(deque)는 O(1)로 접근 가능하다.

# ! 데크는 리스트보다 월등히 빠르다. 따라서 이를 이용하는 것이 좋다.


from collections import deque

deq = deque()

# Add element to the start
deq.appendleft(10)

# Add element to the end
deq.append(0)

# Pop element from the start
deq.popleft()

# Pop element from the end
deq.pop()


#####################################3
# Contain 1, 2, 3, 4, 5 in deq
deq = deque([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
# deque([5, 1, 2, 3, 4])

deq.rotate(-1)
print(deq)
# deque([1, 2, 3, 4, 5])

