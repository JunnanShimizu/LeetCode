class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        
        def dist(x, y):
            return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        
        dists = []

        dists.append(dist(p1, p2))
        dists.append(dist(p1, p3))
        dists.append(dist(p1, p4))
        dists.append(dist(p2, p3))
        dists.append(dist(p2, p4))
        dists.append(dist(p3, p4))

        dists.sort()

        if dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and 0 not in dists:
            return True