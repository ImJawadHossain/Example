from numpy import *
# numpy function

# array Function
"""
stroll = array([1, 8, 'jawad', 48.84])
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""

# linspace Function
# Syntax : linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0 )
"""
stroll = linspace(1, 8, num=5, retstep=True) # এখানে start এবং sotp  এর মান  দেওয়া থাকলে এর মাঝখানের সংখ্যা গুলোকে ৫০ ভাগে ভাগ করবে এবং ডান পাশেরটা থেকে বাম পাশের টা  বিয়োগ করলে সব সময় একই মান পাওয়া যাবে। 
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# logspace Function
# Syntax : logspace(start, stop, num=50, endpoint=True,base=10.0, dtype=None, axis=0 )
"""
stroll = logspace(2, 3, num=5, base= 4)  # এখানে bese  4 এবং start 2 তাই এই 2,  4 এর পাওয়ার হিসেবে কাজ করবে অর্থাৎ start এর মান হয়ে যাবে 16 . আর stop  এর ক্ষেত্রে ও এটি same ভাবে কাজ করে। 
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# arange Function
# Syntax : arange(start=, stop, stepsize, dtype= None)
"""
stroll = arange(1, 8, 2)   # এখানে start আর stop  সিলেক্ট করে দিলে মাঝখানের গুলা প্রিন্ট করবে এটা range ফাঙ্কশন এর মতো কাজ করে 
ln = len(stroll)
print(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""


# zeros Function
# zeros(shape, dtype=float, order='C')
"""
stroll = zeros(5)  #সব জায়গায় 0 দেখাবে 
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""

# ones Function
# ones(shape, dtype=float, order='C')
"""

stroll = ones(5, float, order='F')   #সব জায়গায় 1 দেখাবে 
ln = len(stroll)
for i in range(ln):
    print('index', i, '=', stroll[i])
"""
# any()  fanction
"""
stroll = array([100, 200,300])   #যে কোনো একটা সত্য  হলে true  আসবে আর সব গুলা ভুল হলে false   আসবে 
stroll2 = array([100,466,890])
result = stroll == stroll2
print(any(result))
"""

# any()  fanction
"""
stroll = array([100, 200,300])   # সব গুলি  সত্য  হলে true  আসবে আর যেকোনো একটা  ভুল হলে false   আসবে any(),এবং all ()  or এবং and  এর মতো কাজ করে 
stroll2 = array([100,200,300])
result = stroll == stroll2
print(all(result))
"""

# where() function
# syntax: numpy.where(condition,expretion1,expression2)
"""
a = array([100, 200,360])   # এটি if  এবং else এর মতো কাজ করে। সত্য হলে  expression1 প্রিন্ট করে আর মিথ্যা হলে expression2 প্রিন্ট করে 
b = array([100, 250, 330])
result = where(a > b, 'right', 'false')
print(result)
"""

# nonzero() function
"""
a = array([100, 200, 300, 0, 400])
b = nonzero(a)        #এটা যেসব ইনডেক্সে 0 থাকে ঐগুলা প্রিন্ট করবে না 
print(b)
"""

# view() Method
"""
a = array([100, 200, 300, 250, 400])
b = a.view()    #লোকেশন বা id আলাদা হবে কিন্তু a  ও b এর যে কোনো একটাই চেঞ্জ করলে অপরটি ও চেঞ্জ হয়ে যাবে 
a[1] = 34
b[2] = 89
print(a)
print(b)
print(id(a))
print(id(b))
"""

# copy() method
"""
a = array([100, 200, 300, 250, 400])
b = a.copy()   #লোকেশন বা id আলাদা হবে এবং  a ও b এর যে কোনো একটাই চেঞ্জ করলে অপরটি ও চেঞ্জ হবে না 
a[1] = 34
b[2] = 89
print(a)
print(b)
print(id(a))
print(id(b))
"""
