# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Base ds01 (py3.7)
#     language: python
#     name: python3
# ---

# # Steven's Advent of Code solutions

# # Imports

import sys
import pathlib
# import math
# import pandas as pd
from itertools import combinations
import numpy as np

base = pathlib.Path('/home/steve/AOC/')
raw = base / 'inputs'

import os
cwd = os.getcwd()

cwd

# ## Question 1

# ## Part 1
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
#
# ## Part 2
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?

# ### File read

fname = "q1.txt"
file = raw / fname
f = open(file, "r")

# ## Part 1 answer OLD

alist = []
for x in f:
    alist.append(x)

for x, i in enumerate(alist, 0):
    alist[x] = alist[x].strip("\n")

for x, i in enumerate(alist, 0):
    for j in alist[x+1:]:
        if int(i)+int(j) == 2020:
            print(int(i)*int(j))

# ## Part 2 answer OLD

for x, i in enumerate(alist, 0):
    for j in alist[x+1:]:
        for y in alist[x+2:]:
            if int(i)+int(j)+int(y) == 2020:
                print(int(i)*int(j)*int(y))

# ## Part 1 clean

qlist = list(map(int, (x.strip() for x in f.readlines())))

for x in combinations(qlist, 2):
    if sum(x) == 2020:
        print(np.product(x))
        break

# ## Part 2 clean

for x in combinations(qlist, 3):
    if sum(x) == 2020:
        print(np.product(x))

# # Question 2

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
#
# For example, suppose you have the following list:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
#
# How many passwords are valid according to their policies?

# ## File read

fname = "q2.txt"
file = raw / fname
f = open(file, "r")

# ## Part 1 answer

qlist = [x.strip().split() for x in f.readlines()]

countv = 0
for x in qlist:
    lo, hi = list(map(int, x[0].split('-')))
    char = x[1][0]
    countv += lo <= x[2].count(char) <= hi
print(countv)

# ## Part 2 answer

countv2 = 0
for x in qlist:
    # cba to confine same vars into one
    lo, hi = list(map(int, x[0].split('-')))
    char = x[1][0]
    countv2 += (x[2][lo - 1] == char) ^ (x[2][hi - 1] == char)
print(countv2)
