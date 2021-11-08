from math import gcd
def solution(s1, s2):
    GCD = gcd(len(s1), len(s2))
    if GCD == 1 and len(s1) > 1 and len(s2) > 1:
        return ""
    else:
        if len(s1) == GCD:
            return s1
        else:
            return s2

s1 = 'abababab'
s2 = 'abab'

print(solution(s1, s2))