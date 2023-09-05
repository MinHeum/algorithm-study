class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point):
            return point[0]**2 + point[1]**2
        points.sort(key=get_distance)
        return points[:k]
    