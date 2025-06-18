class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row, col = len(board), len(board[0])

        self.exist = False
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        def dfs(i,j,count) :
            if self.exist :
                return
            
            if count == len(word):
                self.exist = True
                return
            visited.add((i,j))
            for x,y in direction :
                nx,ny = i+x, j+y
                if 0 <= nx < row and 0 <= ny < col and (nx,ny) not in visited and board[nx][ny] == word[count] :
                    dfs(nx,ny, count + 1)
            visited.remove((i,j))
                    

        for i in range(row):
            for j in range(col) :
                if board[i][j] == word[0] :
                    dfs(i,j,1)
                
        
        return self.exist
            


        