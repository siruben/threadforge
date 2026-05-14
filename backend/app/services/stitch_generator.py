import math
from typing import List, Tuple

class Stitch:
    def __init__(self, x: float, y: float, cmd: str = "move"):
        self.x = x
        self.y = y
        self.cmd = cmd

class StitchPath:
    def __init__(self):
        self.stitches = []
    def add_stitch(self, x, y, cmd="stitch"):
        self.stitches.append(Stitch(x,y,cmd))
    def simplify(self, tolerance=1.0):
        if len(self.stitches) <= 2:
            return
        simplified = []
        for s in self.stitches:
            if not simplified or math.hypot(s.x - simplified[-1].x, s.y - simplified[-1].y) > tolerance:
                simplified.append(s)
        self.stitches = simplified

def generate_stitches(svg_paths, density=1.0, min_stitch_length=2, max_stitch_length=20, stitch_type="satin", fabric="cotton"):
    all_stitches = []
    for svg_path in svg_paths:
        if not svg_path.points:
            continue
        sp = StitchPath()
        x0,y0 = svg_path.points[0]
        sp.add_stitch(x0, y0, "move")
        if stitch_type == "running":
            pts = _generate_running_stitches(svg_path.points, density)
        elif stitch_type == "fill":
            pts = _generate_fill_stitches(svg_path.points, density)
        else:
            pts = _generate_satin_stitches(svg_path.points, density)
        for px,py in pts:
            sp.add_stitch(px,py,"stitch")
        sp.simplify(max_stitch_length)
        all_stitches.extend(sp.stitches)
        all_stitches.append(Stitch(x0,y0,"end"))
    return all_stitches

def _interpolate_points(p1, p2, step):
    distance = math.hypot(p2[0]-p1[0], p2[1]-p1[1])
    if distance == 0:
        return [p1]
    steps = max(1, int(distance / max(1, step)))
    pts = []
    for i in range(steps+1):
        t = i/steps
        x = p1[0] + (p2[0]-p1[0]) * t
        y = p1[1] + (p2[1]-p1[1]) * t
        pts.append((x,y))
    return pts

def _generate_running_stitches(points, density):
    s = []
    for i in range(len(points)-1):
        s += _interpolate_points(points[i], points[i+1], density*2)
    return s

def _generate_satin_stitches(points, density):
    s = []
    for i in range(len(points)-1):
        s += _interpolate_points(points[i], points[i+1], density)
    return s

def _generate_fill_stitches(points, density):
    s = []
    for i in range(len(points)-1):
        s += _interpolate_points(points[i], points[i+1], density*0.5)
    return s
