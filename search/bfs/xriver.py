#!/usr/bin/python

def solve():
    s = []
    queue = [[(0xf, 0)]]
    while queue != []:
        cur = queue.pop(0)
        if cur[0] == (0, 0xf):
            s.append(reverse(cur))
        else:
            for m in moves(cur):
                queue.append([m]+cur)
    return s

def moves(s):
    (a, b) = s[0]
    return valid(s, trans(a, b) if b < 8 else swaps(trans(b, a)))

def valid(s, mv):
    return [(a, b) for (a, b) in mv if a not in [3, 6] and b not in [3, 6] and (a, b) not in s]

def trans(a, b):
    masks = [ 8 | (1<<i) for i in range(4)]
    return [(a ^ mask, b | mask) for mask in masks if a & mask == mask]

def swaps(s):
    return [(b, a) for (a, b) in s]

def reverse(x):
    return x[::-1]

def pretty_print(s):
    for ms in s:
        for (a, b) in ms:
            print wgc(a), "====", wgc(b)
        print "total", len(ms) - 1, "steps"
    print "total", len(s), "soluitons"

def wgc(x):
    return [n for (i, n) in [(1, "wolf"), (2, "goat"), (3, "cabbage"), (4, "farmer")] 
              if (x & i) != 0]

pretty_print(solve())
