# This program generates the fibonacci sequence to the Nth number
N = int(input("How many terms of the fibonacci sequence should be generated?"))
t1 = 1
tn = 1
tbefore = 0
counter = 1
if N == 0:
    print()
else:
    print(t1)
    while counter < N:
        print(tn)
        tbefore = tn - tbefore
        tn = tbefore + tn
        counter += 1
