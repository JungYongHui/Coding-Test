from collections import deque


def solution(priorities, location):
    answer = 0

    deq = deque([(i, idx) for idx, i in enumerate(priorities)])
    print(deq)
    print(max(deq))

    while deq:
        pri, idx = deq.popleft()

        if deq and pri < max(deq)[0]:
            deq.append((pri, idx))
        else:
            answer += 1
            if idx == location:
                break
    return answer