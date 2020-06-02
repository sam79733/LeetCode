"""  Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Hingt- A line would be straight if slop between all coordinates will be same. A line between two points will always straight.
formula= slop between two point- (x0,y0), (x1,y1)
	slop = (y1-y0) / (x1-x0)
	


Solution
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(len(coordinates) == 2):
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x,y = coordinates[i]
            if((y1-y0) * (x- x0) != (y-y0) * (x1-x0)):
                return False
        return True