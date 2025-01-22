target = 4
r = 1
rs = 0
rm = 0

while (r <= target):
    rs = r ** 2
    print(rs)
    rm = r % 4
    print(rm)
    r = r + 1
    print(r)