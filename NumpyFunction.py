from numpy import *
# numpy function

# array Function
"""
stroll = array([1, 8, 'jawad', '48.84'])
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""

# linspace Function
# Syntax : linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0 )
"""
stroll = linspace(1, 8, num=5, retstep=True)
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# logspace Function
# Syntax : logspace(start, stop, num=50, endpoint=True,base=10.0, dtype=None, axis=0 )
"""
stroll = logspace(2, 3, num=5, base= 4)  # here start as 16 and stop as 64 because here show start and stop as a power to the base.
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# arange Function
# Syntax : arange(start=, stop, stepsize, dtype= None)
"""
stroll = arange(1, 8, 2)   # Its as same as range function
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# zeros Function
# zeros(shape, dtype=float, order='C')
"""
stroll = zeros(5)
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""

# ones Function
# ones(shape, dtype=float, order='C')

stroll = ones(5, float, order='F')
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
