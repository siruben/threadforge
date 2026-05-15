import struct

class PESExporter:
    def __init__(self, thread_color="#000000"):
        self.thread_color = thread_color
        self.stitches = []

    def add_stitches(self, stitches):
        self.stitches = stitches

    def export(self, file_path):
        with open(file_path, "wb") as f:
            f.write(b'#PES0050')
            f.write(b'\\x00'*8)
            for s in self.stitches:
                x = int(s.x * 10) & 0xFFFF
                y = int(s.y * 10) & 0xFFFF
                cmd = 1 if s.cmd=="stitch" else 0
                f.write(struct.pack('<HHB', x, y, cmd))
            f.write(struct.pack('<HH', 0,0))

def export_pes(stitches, file_path, thread_color="#000000"):
    e = PESExporter(thread_color)
    e.add_stitches(stitches)
    e.export(file_path)
