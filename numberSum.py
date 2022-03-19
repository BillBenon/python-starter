def numCount(num):
    count = 0
    remaining = 0
    while (num >= 9):
        num = num - 9
        count = count+1
        remaining = num
    print(remaining, count)


numCount(13371337)
