import xml.etree.ElementTree as ET
import re
from typing import List, Tuple

class SVGPath:
    def __init__(self, d: str, fill: str = "#000000"):
        self.d = d
        self.fill = fill
        self.points = self.parse_path_data(d)

    @staticmethod
    def parse_path_data(d: str):
        coords = re.findall(r'[-+]?\d*\.?\d+', d)
        points = []
        for i in range(0, len(coords), 2):
            if i+1 < len(coords):
                points.append((float(coords[i]), float(coords[i+1])))
        return points

def parse_svg(file_path: str):
    tree = ET.parse(file_path)
    root = tree.getroot()
    paths = []
    for path_elem in root.findall('.//{http://www.w3.org/2000/svg}path'):
        d = path_elem.get('d', '')
        fill = path_elem.get('fill', '#000000')
        if d:
            paths.append(SVGPath(d, fill))
    for circle in root.findall('.//{http://www.w3.org/2000/svg}circle'):
        cx = float(circle.get('cx', 0))
        cy = float(circle.get('cy', 0))
        r = float(circle.get('r', 0))
        points = []
        import math
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            x = cx + r * math.cos(rad)
            y = cy + r * math.sin(rad)
            points.append((x, y))
        p = SVGPath('', '#000000')
        p.points = points
        paths.append(p)
    return paths
