# 이름 끝에 철자 'm'을 가진 사람이 망고 판매상이다.
# 본인의 지인을 포함한 지인의 지인을 탐색하여 망고 판매상을 찾아라.

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def search(name):
    search_queue = deque([name]) # 첫 스타트
    searched = []
    
    def person_is_seller(naming):
        return naming[-1] == 'm'
    
    while search_queue: 
        person = search_queue.popleft()
        search_queue += graph[person] 
        
        if person_is_seller(person):
            print(person + ' is a mango seller!')
            searched.append(person)
            return True
        
    if len(searched) == 0:
        print('There is not seller!')

search('you')