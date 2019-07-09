from itertools import combinations
number ,b = input().split()
b = int(b)
snumber = []
g = combinations(number,len(number)-b)
for i in g:
    snumber.append("".join(i))
print(min(snumber))
