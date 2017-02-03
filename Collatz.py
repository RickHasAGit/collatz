#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# Rico C. Swan
# ---------------------------

globmemotab = {}

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read an int from r
    r a reader
    return the int
    """
    n = int(r.readline())
    assert n > 0
    return n

# --------------
# collatz_length
# --------------

def collatz_length (r) :
    """
    calculates cycle length for a number
    r a number
    return the int
    """

    assert r > 0

    global globmemotab
    if r in globmemotab:
        return globmemotab[r]
    if r == 1:
        return 1
    if r % 2 == 0:
        globmemotab[r] = 1 + collatz_length(r/2)
        return globmemotab[r]
    globmemotab[r] = 1 + collatz_length(r*3 +1)
    assert globmemotab[r] > 0
    return globmemotab[r]

# ------------
# collatz_eval
# ------------

def collatz_eval (n) :
    """
    n the end of the range [1, n], inclusive
    return the max cycle length of the range [1, n]
    """
    # <your code>

    if n < 5000000 :
        metacache = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]
        for i in range(len(metacache)) :
            if metacache[i] > n :
                return metacache[i-1]
        return metacache[-1]


    if n == 1:
        return 1
    q = 1
    p = 1
    for i in range(n//2, n):
        if collatz_length(i) >= q:
            q = collatz_length(i)
            p = i
    return p


# ------------
# collatz_meta
# ------------

def collatz_meta (n) :
    """
    n the end of the range [1, n], inclusive
    return the max cycle length of the range [1, n]
    """
    q = 1
    p = 1
    for i in range(1, n):
        if collatz_length(i) >= q:
            q = collatz_length(i)
            p = i
            print( str(p))

# -------------
# collatz_print
# -------------

def collatz_print (w, m) :
    """
    print an int to w
    w a writer
    m the max cycle length
    """
    assert m > 0
    w.write(str(m) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    t = int(r.readline())
    for _ in range(t) :
        n = collatz_read(r)
        m = collatz_eval(n)
        collatz_print(w, m)
