class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

        comb = len(digits)

        res = []
        letCom = ''

        if comb == 0 :
            return res

        def dfs(size, letCom) :

            if size == comb :
                res.append(letCom)
                return
            
            for c in letter[int(digits[size])-2]:
                letCom += c.lower()
                dfs(size+1, letCom)
                letCom = letCom[:-1]
            
        
        dfs(0,letCom)

        return res

            

