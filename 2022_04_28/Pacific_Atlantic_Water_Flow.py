#릿코드 417번 (그래프)
'''처음에 통과 못한 이유
방문처리를 2차원리스트를 만들어서 했는데, 이 방법의 경우 입력크기가 크면,
방문처리용 리스트를 만드는데만 많은 시간이 걸리기 떄문에, set을 이용ㅇ했다.
예를 들면 방문처리를 위해 만들어야되는 크기가 10억*10억인데, 실제로는 2개만 방문하면 메모리, 속도 면에서 모두 낭비이다.
따라서 set을 이용해서 처리하는 방법으로 바꿨다.
'''
from collections import deque


class Solution:

    def pacificAtlantic(self, heights)-> int:

        m = len(heights)
        n = len(heights[0])

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        result = list()

        def bfs(start_node:list,visited)->bool:

            need_visited = deque()
            need_visited.append(start_node)

            pacific_flag = False
            Atlantic_flag = False

            while need_visited:
                
                current_r, current_c = need_visited.popleft()

                if current_r == 0 or current_c == 0:
                    pacific_flag = True

                if current_r == m-1 or current_c == n-1:
                    Atlantic_flag = True

                if pacific_flag == True and Atlantic_flag == True:
                    return True

                for i in range(4):
                    next_r = current_r + dx[i]
                    next_c = current_c + dy[i]

                    if (0<= next_r < m) and (0 <= next_c < n) and heights[next_r][next_c] <= heights[current_r][current_c] and (next_r,next_c) not in visited:
                        # print(next_r,next_c)
                        visited.add((next_r,next_c))
                        need_visited.append([next_r,next_c])
                        
            return False

        for i in range(m):
            for j in range(n):
                
                visited = set()
                visited.add((i,j))

                if bfs([i,j],visited) == True:
                    result.append([i,j])

        return result

'''시간초과 난 코드

from collections import deque

class Solution:
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(self,heights:list,start_node:list)->bool:
        m = len(heights)
        n = len(heights[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        need_visited = deque()
        need_visited.append(start_node)

        visited[start_node[0]][start_node[1]] = 1

        pacific_flag = False
        Atlantic_flag = False

        ## start_node check
        for i in range(4):
            if start_node[0] + self.dx[i] == -1 or start_node[1] + self.dy[i] == -1:
                pacific_flag = True
        
            if start_node[0] + self.dx[i] == m or start_node[1] + self.dy[i] == n:
                Atlantic_flag = True

        if pacific_flag == True and Atlantic_flag == True:
                return True

        while need_visited:
            
            current_r, current_c = need_visited.popleft()

            for i in range(4):
                next_r = current_r + self.dx[i]
                next_c = current_c + self.dy[i]

                if (0<= next_r < m) and (0 <= next_c < n):
                    if heights[next_r][next_c] <= heights[current_r][current_c] and visited[next_r][next_c] == 0:
                        visited[next_r][next_c] = 1
                        need_visited.append([next_r,next_c])

                else:
                    ## 0: only pacific, 1: only Atlantic, 2: Both
                    ## r == -1,c == -1 => pacific, r == n, c == n  => Atlantic
                    if next_r == -1 or next_c == -1:
                        pacific_flag = True
                
                    if next_r == m or next_c == n:
                        Atlantic_flag = True
                    
                
                if pacific_flag == True and Atlantic_flag == True:
                    return True
                

        return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        result = list()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if self.bfs(heights,[i,j]) == True:
                    result.append([i,j])

        return result



'''        


if __name__ =="__main__":

    a = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    assert a.pacificAtlantic(heights) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    heights = [[2,1],[1,2]]
    assert a.pacificAtlantic(heights) == [[0,0],[0,1],[1,0],[1,1]]


    #에러난 테케
    heights = [[1,1],[1,1],[1,1]]
    print(a.pacificAtlantic(heights))