# the code was copied from "Submitted code" field
# https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    return ' '.join(map(str.capitalize, s.split(' ')))