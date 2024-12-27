def find_second_maximum(num):
    
    max_num = int()
    second_max_num = int()
    
    for num in num:
        if int(num) > max_num:
            second_max_num =max_num
            max_num = num
        elif int(num) > second_max_num:
            second_max_num =num
    
    return second_max_num

# Example usage:
a= int (input())
num = input().split()
second_max = find_second_maximum(num)
print(second_max)
