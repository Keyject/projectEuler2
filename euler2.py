# euler2
# KeyJect
e1 = 1
e2 = 2
ans = 2
while True:
    e3 = e1 + e2
    if e3>=4000000:
        break
    if e3%2==0:
        ans += e3
    e1 = e2
    e2 = e3
print(ans)