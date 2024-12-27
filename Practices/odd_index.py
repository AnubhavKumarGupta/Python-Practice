n = input()

for i in n:
    # print(f"{i} = {n.index(i)}")
    if n.index(i) % 2 != 0:
        print(f"At {n.index(i)} index the character is = {i}  ")
