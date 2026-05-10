def pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n=int(input("Enter n: "))
    pattern(n)