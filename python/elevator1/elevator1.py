from multiprocessing import Pool
import sys

def f(elevator_name):
    # try:
    #     new_floor = int(raw_input("Floor?:"))
    #     if new_floor <= 0 :
    #         raise
    # except:
    #     print("invalid input")
    #     exit(0)

    new_floor = int(input("Floor?:"))
    print("Elevator[{}]{}".format(elevator_name,"-" * new_floor ))
    sys.stdout.flush()

    return(elevator_number, current_floor, requested_floor)

if __name__ == '__main__':
    with Pool(3) as p:
        elevators = ["one","two","three"]
        while True:
            p.map(f, elevators)

