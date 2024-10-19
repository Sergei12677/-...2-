from turtledemo.chaos import jumpto

result = ''
for n in range(3,21):
    temp_password = ''
    for i in range(1,n):
        for j in range(i+1,n+1):
             pair_sum = i+j
             if n % pair_sum == 0:
                 temp_password+=f"{i}{j}"
                 result+= f"{n}-{temp_password}n"
                 print(result)

