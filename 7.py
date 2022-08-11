x_boom = 7
for i in range(1, 100):
    if i % x_boom == 0 or str(x_boom) in str(i):
        continue
    print(i)

else:
    print("loop finished successfuly")
    # my comment
