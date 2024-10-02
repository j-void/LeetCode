class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people.sort(key=lambda x:(-x[0], x[1]))

        for i in range(len(people)):
            queue.insert(people[i][1], people[i])
        
        return queue
        
        
