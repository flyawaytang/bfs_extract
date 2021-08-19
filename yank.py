import sys
import struct

class BFS:
  def __init__(self, data):
    self.data = data

  @classmethod
  def open(cls, path):
    with open(path, 'r+b') as f:
      f.seek(-12, 2)
      magic_chunk = f.read(12)
      pointer_header = struct.unpack('<III', magic_chunk)
      assert(pointer_header[0] == 0xab2155bc)

      f.seek(-12 - pointer_header[2], 2)
      data = f.read(pointer_header[2])
      return cls(data)

bfs = BFS.open(sys.argv[1])
with open(sys.argv[2], 'wb') as outf:
  outf.write(bfs.data)
