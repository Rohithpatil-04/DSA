# num=125
# sum=0
# while(num>0):
#     sum+= num%10
#     num=num//10
# print(sum)

num=int(input("enter number:"))
sum=0
n=num
while(num>0):
    sum=sum*10+(num%10)
    num//=10
if(n==sum):
    print("number is palidrome")