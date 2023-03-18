n, m = map(int, input().split())
w = [0 for i in range(n+1)]
v = [0 for i in range(n+1)]
dp = [0 for i in range(m+1)]

for i in range(1, n+1):
    wi, vi = map(int, input().split())
    w[i] = wi
    v[i] = vi

for i in range(1, n+1):
    for j in range(m, w[i]-1, -1):
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])

print(dp[m])
