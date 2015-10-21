"""
Finish the solution so that it takes an input 'n' (integer) and returns a string
that is the decimal representation of the number grouped by commas after every
3 digits.

Assume: 0 <= n < 1000000000

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""

""" Naive Solution
def group_by_commas(n):
    str_lst = list(str(n))
    str_lst.reverse()
    for i in range(0, len(str_lst)):
        if i % 3 == 0 and i > 0:
            str_lst[i] = str_lst[i] + ','
    str_lst.reverse()
    return ''.join(str_lst)
"""

# Better Solution
def group_by_commas(n):
    return '{:,}'.format(n)
print group_by_commas(35353231555)
