"""
A | 1
B | 2
C | 3
D | 4
E | 5
F | 6
G | 7
H | 8
I | 9
J | 10
K | 11
L | 12
M | 13
N | 14
O | 15
P | 16
Q | 17
R | 18
S | 19
T | 20
U | 21
V | 22
W | 23
X | 24
Y | 25
Z | 26
"""
from string import ascii_uppercase


def number_to_alpha(num: int) -> str:
    if num // 26 == 0:
        return ascii_uppercase[num - 1]
    return number_to_alpha(num // 26) + ascii_uppercase[num % 26 - 1]


def alpha_to_number(alpha_num: str, digit_pointer: int = 0) -> int:
    def processor(alpha_num):
        if len(alpha_num) == 1:
            return ascii_uppercase.index(alpha_num[digit_pointer]) + 1
        return (ascii_uppercase.index(alpha_num[digit_pointer]) + 1) * 26 ** (len(alpha_num) - 1) + processor(alpha_num[1:])

    return processor(alpha_num.upper())
