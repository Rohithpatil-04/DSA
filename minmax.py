arr=[10,25,50,32,99,26,46,33]
min =arr[0]
max=arr[0]
for num in arr:
    if num<min:
        min=num
    if num>max:
        max=num
print("minimum number is",min)
print("maximun number",max)
        