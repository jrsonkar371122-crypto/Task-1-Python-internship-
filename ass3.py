print("Enter 5 numbers:")
list=[]
for i in range(5):
    numbers=int(input())
    list.append(numbers)
print(list)

total=0
for i in list:
    total=total+i
    avg=total/len(list)

print(f"Sum={total}")
print(f"Average={avg}")
print(f"{max(list)}")