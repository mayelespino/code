#https://docs.python.org/3/reference/datamodel.html#special-method-names
class DataPoints(object):
    def __init__(self,pointA, pointB):
        self.pointA=pointA
        self.pointB=pointB
    def __add__(self, dataPoint):
        sumA = self.pointA + dataPoint.pointA
        sumB = self.pointB + dataPoint.pointB
        return DataPoints(sumA,SumB)
    def _assign__(self,dataPoint):
        self__init__(dataPoint)
    def __str__(self):
        return (self.pointA, self.pointB)

if __name__ == '__main__':
    dp = DataPoints(1,2)
    dp1 = DataPoints(2,3)
    dp2 = dp + dp1 
    print dp2 + dp
#expected result
(4,7)    
    #Before
    print dp1 + dp
(3,5)
    
    
