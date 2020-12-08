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
import re

base = pathlib.Path('/home/steve/AOC/AOC2020/Steve_Code')
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

fname = "q1.txt"
file = raw / fname
f = open(file, "r")

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

# # Question 3

# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:
#
# ```..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# ```
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
#     
# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
# ```
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# ```
#
# In this example, traversing the map using this slope would cause you to encounter 7 trees.
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

# ## File read

fname = "q3.txt"
file = raw / fname
f = open(file, "r")

# ## Part 1

treeI = [x.strip() for x in f.readlines()]


def count_trees(slope_x, slope_y):
    x = 0
    y = 0
    trees = 0
    while y < len(treeI):
        trees += treeI[y][x % len(treeI[0])] == '#'
        x += slope_x
        y += slope_y
    return trees


print(count_trees(3, 1))

print( count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1)
    * count_trees(7, 1) * count_trees(1, 2))

# ## Question 4

# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
#
# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
# ```
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# ```
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
# ```
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# ```
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).
# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.
# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.
# According to the above rules, your improved system would report 2 valid passports.
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

# ### File read

fname = "q4.txt"
file = raw / fname
f = open(file, "r")

# ### Part 1

data = f.read()

passports = []
for block in data.split('\n\n'):
    parsed = re.findall(r'(\w+):(\S+)', block)
    passports.append({m[0]: m[1] for m in parsed})

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


# +
def is_valid(passport):
    return not any(required - passport.keys())


print(sum(map(is_valid, passports)))


# -

# ### Part 2

# +
def is_valid(passport):
    # Abuse exceptions for control flow
    try:
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002: return False
        
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020: return False
        
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030: return False
        
        hgt = passport['hgt']
        match = re.match(r'(\d+)(cm|in)', hgt)
        height, unit = match[1], match[2]
        
        if unit == 'cm':
            if not 150 <= int(height) <= 193:
                return False
        elif unit == 'in':
            if not 59 <= int(height) <= 76:
                return False
        else: return False
        
        hcl = passport['hcl']
        if hcl[0] != '#' or len(hcl) != 7: return False
        
        int(hcl[1:], 16)  # Raises exactly if the desired criterion fails
        ecl = passport['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): 
            return False
        
        pid = passport['pid']
        if not pid.isdigit() or len(pid) != 9: return False
        
        return True
    except:
        return False

print(sum(map(is_valid, passports)))
# -

# ## Question 5

# ```
# he first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
#
# For example, consider just the last 3 characters of FBFBBFFRLR:
#
# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
#
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
#
# Here are some other boarding passes:
#
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
# ```

# ### File read

fname = "q5.txt"
file = raw / fname
f = open(file, "r")

# ### Part 1

ls = [x.strip() for x in f.readlines()]


# +
def binary(w):
    w = re.sub('[FL]', '0', w)
    w = re.sub('[BR]', '1', w)
    return int(w, 2)

print(max(map(binary, ls)))
# -

# ### Part 2

all_ids = sorted(list(map(binary, ls)))
def find_missing(lst): 
    start = lst[0] 
    end = lst[-1] 
    return sorted(set(range(start, end + 1)).difference(lst))
print(*find_missing(all_ids)) 

# ### Day 6

# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
#
# However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
# ```
# abcx
# abcy
# abcz
# ```
# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)
#
# Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:
# ```
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
# ```
# This list represents answers from five groups:
#
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
#
# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

# ### File read

fname = "q6.txt"
file = raw / fname
f = open(file, "r")

# ### Part 1

 groups = f.read().strip().split('\n\n')

print(sum(len(set(g.replace('\n', ''))) for g in groups))

# ### Part 2

print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))

# ## DAY 7

# ue to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!
#
# For example, consider the following rules:
# ```
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# ```
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.
#
# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
#
# In the above rules, the following options would be available to you:
#
# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.
#
# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

# ### Import/File read

# jupyter inline pip install because I was lazy and forgot to make a new conda env for this AOC
!{sys.executable} -m pip install networkx

# Makes find a predecessor in a directed tree later on a lot easier
import networkx as nx


fname = "q7.txt"
file = raw / fname
f = open(file, "r")

# ### Part 1

data = [x.strip().split() for x in f.readlines()]

rules = {}
for w in data:
    parent = w[0] + w[1]
    i = 4
    contains = []
    while i < len(w) and w[i] != 'no':
        count = int(w[i])
        child = w[i+1] + w[i+2]
        contains.append((count, child))
        i += 4
    rules[parent] = contains

G = nx.DiGraph()
for colour, contains in rules.items():
    for x, child in contains:
        G.add_edge(child, colour)
print(len(nx.predecessor(G, 'shinygold')) - 1)


# ### Part 2

# +
def num_bags(colour):
    return 1 + sum(count * num_bags(child) for count, child in rules[colour])


print(num_bags('shinygold') - 1)
# -

# ## Q8

# Their handheld game console won't turn on! They ask if you can take a look.
#
# You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.
#
# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
#
# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# For example, consider the following program:
# ```
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# ```
# These instructions are visited in this order:
# ```
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
# ```
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.
#
# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.
#
# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
#
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?

# ### File read

fname = "q8.txt"
file = raw / fname
f = open(file, "r")

# ### Part 1

ws = [line.strip().split() for line in f.readlines()]

instructions = [w[0] for w in ws]
values = [int(w[1]) for w in ws]


def run(insts, values):
    i = 0
    seen = set()
    acc = 0
    while True:
        if i in seen:
            return (False, acc)
        seen.add(i)
        inst = insts[i]
        value = values[i]
        if inst == 'acc':
            acc += value
        if inst == 'jmp':
            i += value
        else:
            i += 1


x, acc = run(instructions, values)
print(acc)

# ### Part 2


