
def fibunacci(target):
    fibb, prev = 0,1
    for x in range(target):
        fibb, prev = prev+fibb, fibb
    return(fibb)

def main():
    print("Fibunnaci 10.")
    print(fibunacci(10))
    print("Fibunnaci 100.")
    print(fibunacci(100))


if __name__ == '__main__': main()