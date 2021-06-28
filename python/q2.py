pos=1
num=1
odd_numbers = []
while pos<=100:
    if num%2 == 0:
        num=num+1
        continue
    else:
        odd_numbers.append(num)
        num=num+1
        pos=pos+1           
print (odd_numbers)