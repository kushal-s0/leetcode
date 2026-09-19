class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closex=max(x1,min(x2,xCenter))
        closey=max(y1,min(y2,yCenter))
        dx=xCenter-closex
        dy=yCenter-closey
        return (dx**2+dy**2<=radius**2)