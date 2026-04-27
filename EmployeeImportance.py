from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_profile = dict()
        total = 0

        for employee in employees:
            employees_profile[employee.id] = employee

        def DFS(employee_id):
            nonlocal total
            employee = employees_profile[employee_id]
            total += employee.importance

            for emp_id in employee.subordinates:
                DFS(emp_id)

        DFS(id)
        return total
