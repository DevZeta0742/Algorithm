def ccw(a: list, b: list, c: list):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def convex_hull(points: list):
    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
            
        lower.append(p)
        
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
            
        upper.append(p)
        
    return lower[:-1] + upper[:-1]

def dist(a: list, b: list):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def rotating_calipers(hull: list):  # 가장 먼 두 점 찾기
    n = len(hull)
    r = 0
    ans = 0
    for i in range(n):
        while r < n * 2 and ccw(hull[i], hull[(i + 1) % n], (hull[(i + 1) % n][0] + hull[(r + 1) % n][0] - hull[r % n][0], hull[(i + 1) % n][1] + hull[(r + 1) % n][1] - hull[r % n][1])) >= 0:
            ans = max(ans, dist(hull[i], hull[r % n]))
            r += 1
            
        ans = max(ans, dist(hull[i], hull[r % n]))
        
    return ans
