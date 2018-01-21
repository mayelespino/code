#
# Simple program to ilustrate a race condition.
# for example start one instance wit 5 and 
# another instance with -5 
#
import time, sys

def read_file():
    try:
        with open("memory.txt","r") as f:
            memory_var = f.read()
    except:
        memory_var = 0

    return(int(memory_var))

def write_file(variable):
    with open("memory.txt", "w") as f:
        f.write("{}".format(variable))

def main():
    if len(sys.argv) < 2:
        print("must provide a non-zero number(positive or negative).")
        sys.exit(0)
    else:
        operator = int(sys.argv[1])
        wait_time = abs(operator)

    rogue_var = read_file()
    if rogue_var == 0:
        rogue_var = operator
        write_file(rogue_var)

    while rogue_var >= 0: 
        print("{}|{}|{}".format(rogue_var,wait_time,operator))
        time.sleep(wait_time)
        rogue_var = read_file() + operator
        write_file(rogue_var)
    rogue_var = read_file()
    print("Exiting becase rogue_var is: {}\n".format(rogue_var))

if __name__ == "__main__": main()
