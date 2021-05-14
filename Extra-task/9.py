""" Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
NOTE: Make sure to avoid counting the occurrence of numeric values in the string. """

from typing import Counter
import re

input="12abcdabcfr45you"
result = re.sub('[\d_]+', '', input)
print(result)
z=Counter(result)
print(z)

