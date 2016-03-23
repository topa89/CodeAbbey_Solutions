n=int(input())
answer=[]
for i in range(n):
    one=0
    two=0
    a=input().split()
    for words in a:
        if words[0]==words[1]:
            continue
        else:
            if words in ['RS', 'PR', 'SP']:
                one+=1
            else:
                two+=1
    if one>two:
        answer.append('1')
    else:
        answer.append('2')
print(' '.join(answer))
