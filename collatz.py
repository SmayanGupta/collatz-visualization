import matplotlib.pyplot as plt


def collatz(n):
    step=0
    if n == 1:
        return 1
    else:
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                n=3*n+1
            step+=1
            #print(n)
        return step
#print(collatz(670617279))
plt.plot([1,2,3,4])
plt.axis("off")
plt.show()