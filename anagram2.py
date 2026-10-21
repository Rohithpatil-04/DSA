def countfreq(n):
    freq=[0]*10


    while(n!=0):
        last_digit=n%10
        freq[last_digit]+=1
        n//=10

    return freq

n=121352133321555

res=countfreq(n)
k=3
l=[]
for i in range(len(res)):
    if res[i]>=k:
        l.append(i)

print(l)