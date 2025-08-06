#sum numbers.py
num_str=input("enter a positive integer: ")
n=int(num_str)

total_sum=0
for current_num in range(1,51):
    total_sum+= current_num
    print(f"adding{current_num}.current sum:{total_sum}")
    print(f"\n the final sum of numbers 1 to 50 is: {total_sum}")





