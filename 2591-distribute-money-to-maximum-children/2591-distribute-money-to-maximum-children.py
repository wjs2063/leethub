class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 최소한 1달러는 가져야 하며 
        # 4달러는 가지면안되고 
        # 8달러를 가진 학생의 최댓값 
        """
        1달러를 먼저 다 주고 시작
        children - 1 명이 7달러를 가지고, 나머지가 3인게존재하면
        """
        if money < children : return -1
        money -= children
        q,r = divmod(money,7)
        if q == children and r == 0 :
            return children
        if q == children - 1 and r == 3 :
            return children - 2
        return min(children - 1, q)
        
        