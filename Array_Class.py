from array import *

# Append method
"""
stroll = array('i', [101, 102, 203, 104, 105, 106])
stroll.append(107)                                             # extra '107' printed. last position
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""


# Insert method
"""
stroll = array('i', [101, 102, 203, 104, 105, 106])
stroll.insert(1, 100)                                        # extra '100' printed. 1 position
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""


# Pop method
"""
stroll = array('i', [101, 102, 203, 104, 105, 106])
stroll.pop(3)                                            # 3 no. position are removed.
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""

# Removed method
"""
stroll = array('i', [101, 102, 103, 104, 105, 106])
stroll.remove(103)                                            # '103'are removed.
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""

# Index method
"""
stroll = array('i', [101, 102, 103, 104, 105, 106])
ind = stroll.index(103)
print(103, '=', ind, '(index number)')                              # showing '103' no. index [2]
"""

# Reverse method
"""
stroll = array('i', [101, 102, 103, 104, 105, 106])
stroll.reverse()                                            # show all array in Down to Up.
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""

# Extend method
"""
stroll = array('i', [101, 102, 103, 104, 105, 106])
arr = array('i', [107, 108, 109])              # this array is attached with stroll.
stroll.extend(arr)
n = len(stroll)
for i in range(n):
    print(stroll[i], '=', i)
"""

# Print some item

stroll = array('i', [101, 102, 103, 104, 105, 106])
n = stroll[1:4]                                 # its print 1 No. position to 4 No. position
for i in n:
    print(i)
