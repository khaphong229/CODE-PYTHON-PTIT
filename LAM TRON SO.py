def round_number(N):
    rounded_n = ((N + 9) // 10) * 10
    length=len(str(N))
    if length>=2:
	    if int(str(N)[-1])>=5:
		    chin='9'*(length-1)
		    chia='1'+'0'*(length-1)
		    rounded_n=((rounded_n+int(chin))//int(chia))*int(chia)
	    else:
		    chia='1'+'0'*(length-1)
		    rounded_n=((N)//int(chia))*int(chia)
    else:
	    if N>5:
		    rounded_n=10
	    else:
		    rounded_n=N
    return rounded_n

n=int(input())
for _ in range(n):
	N=int(input())
	print(round_number(N))
