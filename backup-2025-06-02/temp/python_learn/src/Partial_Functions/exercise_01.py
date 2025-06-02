# Edit the function provided by calling partial()
#       and replacing the first three variables in func().
# Then print with the new partial function using
#       only one input variable so that the output equals 60.
from functools import partial


def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x


if __name__ == '__main__':
    make_60 = partial(func, 5, 5, 5)
    # 60 - (20+ 15 + 10) = 15
    print(make_60(15))
