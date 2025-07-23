# Named tuple example
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(100, 100)
print(f"Point coordinates: ({p.x}, {p.y})")

# Dataclasses example

from dataclasses import dataclass

@dataclass
class PointData:
    x: int
    y: int
p_data = PointData(200, 200)
print(f"PointData coordinates: ({p_data.x}, {p_data.y})")

# Ordered dict example
from collections import OrderedDict

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

for key, value in od.items():
    print(f"{key}: {value}")

# Default dict example
from collections import defaultdict
dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)
dd['a'].append(3)
for key, value in dd.items():
    print(f"{key}: {value}")

# Deque example
from collections import deque
dq = deque(['a', 'b', 'c'])
dq.append('d')
dq.appendleft('z')
print(f"Deque contents: {list(dq)}")

