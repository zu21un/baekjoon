from fractions import Fraction

N = int(input())
rings = list(map(int, input().split()))
for ring in rings[1:]:
    if rings[0]/ring == rings[0]//ring:
        print(f'{Fraction(rings[0],ring)}/1')
    else:
        print(Fraction(rings[0],ring))