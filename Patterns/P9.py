def pattern1(n):
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*i-1):
            print("*",end="")
        print()

def pattern2(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*i-1):
            print("*",end="")
        print()

if __name__ == "__main__":
    n=int(input("Enter n: "))
    pattern1(n)
    pattern2(n)