"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = defaultdict(list)
        
        for employee in employees:
            _id,imp,sub = employee.id,employee.importance,employee.subordinates
            d[_id].extend([imp,sub])
        
        def dfs(_id):
            res = 0
            res += d[_id][0]
            for child in d[_id][1]:
                res += dfs(child)
            return res
        return dfs(id)

            
        