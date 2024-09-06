from heapq import *
class SummaryRanges:

    def __init__(self):
        self.values = []
        self.intervals = []
        

    def addNum(self, value: int) -> None:
        
        if not self.values:
            self.values.append(value)
            self.intervals.append([value, value])
            return
        
        self.values.append(value)
        changed = False
        for i in range(len(self.intervals)):
            s,e = self.intervals[i]
            if s <= value <= e:
                changed = True
            elif s-value == 1:
                changed = True
                self.intervals[i][0] = value
            elif value-e == 1:
                changed = True
                self.intervals[i][1] = value
        if not changed:
            self.intervals.append([value, value])
                    

        

    def getIntervals(self) -> List[List[int]]:
        if not self.intervals:
            return []
        self.intervals.sort(key=lambda x: x[0])
        start, end = self.intervals[0]
        merged = []
        for i in range(1, len(self.intervals)):
            if end == self.intervals[i][0]:
                end = self.intervals[i][1]
            else:
                merged.append([start, end])
                start, end = self.intervals[i]
        merged.append([start, end])
        self.intervals = merged
        return merged


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
