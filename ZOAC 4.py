H, W, N, M = map(int, input().split())

h_q, h_r = divmod(H, N + 1)
if h_r > 0:
    h_q += 1

w_q, w_r = divmod(W, M + 1)
if w_r > 0:
    w_q += 1

print(h_q * w_q)
