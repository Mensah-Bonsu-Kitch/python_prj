#rounding student grades to the nearest multiple of 5
x = [38, 44, 73, 68, 94, 39]#sample student grades
rnd = []
i = 0
while i < len(x):
    y = divmod(x[i],5)
    if x[i] < 38:
        rnd.append(x[i])
    elif x[i] >= 38 and (5 - y[1]) < 3:
        rnd.append((y[0]*5)+5)
    else:
        rnd.append(x[i])
    i += 1
print(rnd)

