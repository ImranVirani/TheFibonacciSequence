# This program generates the fibonacci sequence to the Nth number
N = int(input("How many terms of the fibonacci sequence should be generated?"))
t1 = 1
tn = 1
tbefore = 0
counter = 1
while N == 0:
    print("You cannot display 0 terms of the fibonacci sequence")
    N = int(input("How many terms of the fibonacci sequence should be generated?"))

print(t1)
while counter < N:
    print(tn)
    tbefore = tn - tbefore
    tn = tbefore + tn
    counter += 1
