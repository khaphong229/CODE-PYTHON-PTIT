def handleNotification(noti):
    words=noti.split()
    while len(' '.join(words))>100:
        words.pop()
    handeledNoti=' '.join(words)
    return handeledNoti

amountTest=int(input())
for test in range(amountTest):
    noti=input()
    print(handleNotification(noti))
