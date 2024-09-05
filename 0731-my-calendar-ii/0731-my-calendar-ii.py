from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.reserve_table = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.reserve_table[start] += 1
        self.reserve_table[end] -= 1
        
        current_book_cnt = 0
        for k in sorted(self.reserve_table):
            current_book_cnt += self.reserve_table[k]
            
            if current_book_cnt >= 3 :
                self.reserve_table[start] -= 1
                self.reserve_table[end] += 1
                return False 
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)