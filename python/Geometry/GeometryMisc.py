import math

EPS = 1e-12

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        return Point(self.x + obj.x, self.y + obj.y)

    def __sub__(self, obj):
        return Point(self.x - obj.x, self.y - obj.y)

    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __div__(self, c):
        return Point(self.x / c, self.y / c)

    def __str__(self):
        return f"({self.x},{self.y})"

def dot(p, q):
    return p.x * q.x + p.y * q.y

def dist2(p, q):
    return dot(p-q, p-q)

def cross(p, q):
    return p.x * q.y - p.y * q.x

# Rotate a point CCW or CC around the origin
def rotateCCW90(p):
    return Point(-p.y, p.x)

def rotateCW90(p):
    return Point(p.y, -p.x)

def rotateCCW(p, t):
    return Point(p.x * math.cos(t) - p.y * math.sin(t), p.x * math.sin(t) + p.y * math.cos(t))

# project point c onto line through a and b
# assuming a != b
def project_point_line(a, b, c):
    return a + (b - a) * dot(c - a, b - a) / dot(b - a, b - a)

# project point c onto line segment through a and b
def project_point_segment(a, b, c):
    r = dot(b - a, b - a)
    if abs(r) < EPS:
        return a

    r = dot(c - a, b - a) / r
    if r < 0:
        return a
    if r > 1:
        return b

    return a + (b - a) * r

# compute distance from c to segment between a and b
def distance_point_segment(a, b, c):
    return math.sqrt(dist2(c, project_point_segment(a, b, c)))

# compute distance between point (x,y,z) and plane ax+by+cz=d
def distance_point_plane(x, y, z, a, b, c, d):
    return abs(a * x + b * y + c * z - d) / math.sqrt(a * a + b * b + c * c)

# determine if lines from a to b and c to d are parallel or collinear
def lines_parallel(a, b, c, d):
    return abs(cross(b - a, c - d)) < EPS

def lines_collinear(a, b, c, d):
    return lines_parallel(a, b, c, d) and abs(cross(a - b, a - c)) < EPS and abs(cross(c - d, c - a)) < EPS

# determine if line segment from a to b intersects with line segment from c to d
def segment_intersect(a, b, c, d):
    if lines_collinear(a, b, c, d):
        if dist2(a, c) < EPS or dist2(a, d) < EPS or dist2(b, c) < EPS or dist2(b, d) < EPS:
            return True
        if dot(c - a, c - b) > 0 and dot(d - a, d - b) > 0 and dot(c - b, d - b) > 0:
            return False
        return True

    if cross(d - a, b - a) * cross(c - a, b - a) > 0:
        return False
    if cross(a - c, d - c) * cross(b - c, d - c) > 0:
        return False
    return True

# compute intersection of line passing through a and b
# with line passing through c and d, assuming that unique
# intersection exists; for segment intersection, check if
# segments intersect first
def compute_line_intersection(a, b, c, d):
    b, d, c = b - a, c - d, c - a
    assert dot(b, b) > EPS and dot(d, d) > EPS
    return a + b * cross(c, d) / cross(b, d)

# compute center of circle given three points
def compute_circle_center(a, b, c):
    b, c = (a + b) / 2, (a + c) / 2
    return compute_line_intersection(b, b + rotateCW90(a - b), c, c + rotateCW90(a - c))

# determine if point q is in a possibly non-convex polygon p (by William
# Randolph Franklin); returns 1 for strictly interior points, 0 for
# strictly exterior points, and 0 or 1 for the remaining points.
# Note that it is possible to convert this into an *exact* test using
# integer arithmetic by taking care of the division appropriately
# (making sure to deal with signs properly) and then by writing exact
# tests for checking point on polygon boundary
def point_in_polygon(p, q):
    c = False
    for i in range(len(p)):
        j = (i + 1) % len(p)
        if (p[i].y <= q.y and q.y < p[j].y or p[j].y <= q.y and q.y < p[i].y) and q.x < p[i].x + (p[j].x - p[i].x) * (q.y - p[i].y) / (p[j].y - p[i].y):
            c = not c
    return c

# determine if point is on the boundary of a polygon
def point_on_polygon(p, q):
    for i in range(len(p)):
        if dist2(project_point_segment(p[i], p[(i + 1) % len(p)], q), q) < EPS:
            return True
    return False

# compute intersection of line through points a and b with
# circle centered at c with radius r > 0
def circle_line_intersection(a, b, c, r):
    ans = []
    a, b = a - c, b - a
    A, B = dot(b, b), dot(a, b)
    C, D = dot(a, a) - r * r, B * B - A * C
    if D < -EPS:
        return ans
    ans.append(c + a + b * (-B + math.sqrt(D + EPS)) / A)
    if D > EPS:
        ans.append(c + a + b * (-B - math.sqrt(D)) / A)
    return ans

# compute intersection of circle centered at a with radius r
# with circle centered at b with radius R
def circle_circle_intersection(a, b, r, R):
    ans = []
    d = math.sqrt(dist2(a, b))
    if d > r + R or d + min(r, R) < max (r, R):
        return ans

    x = (d * d - R * R + r * r) / (2 * d)
    y = math.sqrt(r * r - x * x)
    v = (b - a) / d
    ans.append(a + v * x + rotateCCW90(v) * y)
    if y > 0:
        ans.append(a + v * x - rotateCCW90(v) * y)

    return ans

# This code computes the area or centroid of a (possibly nonconvex)
# polygon, assuming that the coordinates are listed in a clockwise or
# counterclockwise fashion.  Note that the centroid is often known as
# the "center of gravity" or "center of mass".
def compute_signed_area(p):
    area = 0
    for i in range(len(p)):
        j = (i + 1) % len(p)
        area += p[i].x * p[j].y - p[j].x * p[i].y

    return area / 2.

def compute_area(p):
    return abs(compute_signed_area(p))

def compute_centroid(p):
    c = Point(0, 0)
    scale = 6.0 * compute_signed_area(p)
    for i in range(len(p)):
        j = (i + 1) % len(p)
        c = c + (p[i] + p[j]) * (p[i].x * p[j].y - p[j].x * p[i].y)

    return c / scale

# tests whether or not a given polygon (in CW or CCW order) is simple
def is_simple(p):
    for i in range(len(p)):
        for k in range(i + 1, len(p)):
            j = (i + 1) % len(p)
            l = (k + 1) % len(p)
            if i == l or j == k:
                continue
            if segment_intersect(p[i], p[j], p[k], p[l]):
                return False

    return True
