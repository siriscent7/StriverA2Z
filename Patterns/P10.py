def pattern1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

def pattern2(n):
    for i in range(n-1,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()

if __name__ == "__main__":
    n=int(input("Enter n: "))
    pattern1(n)
    pattern2(n)