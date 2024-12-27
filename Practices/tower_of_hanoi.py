def toi(n, s, d, t):
    if n == 1:
        print(f"move disk {n} from {s} to {d}")
        return
    toi(n - 1, s, t, d)
    print(f"move disk {n} from {s} to {d}")
    toi(n - 1, t, d, s)


n = int(input(f"Input the num of tower of hanoi you want\n"))
toi(n, "s", "d", "t")
