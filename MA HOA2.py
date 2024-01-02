def encode_and_reverse(k, s):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    n = len(P)
    encoded_s = ''.join(P[(P.index(c) + k) % n] for c in s)
    reversed_s = encoded_s[::-1]
    return reversed_s

while True:
    user_input = input().split()
    if len(user_input) < 2:
        break
    k, s = user_input
    k = int(k)
    if k == 0:
        break
    print(encode_and_reverse(k, s))
