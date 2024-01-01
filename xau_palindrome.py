# s=input()
# print(len(s)-1)

def max_chars_to_remove(s):
    length=len(s)
    if length==0 or length==1:
        return 0
    cnt=0
    for i in range(length//2):
        if s[i]==s[length-1-i]:
            cnt+=1
    return (cnt*2)-1

s=input()
print(max_chars_to_remove(s))