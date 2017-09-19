from multiprocessing import Pool
import sys

def f(x):
    elevator_number, current_floor, requested_floor = x
    if current_floor <= 0 or requested_floor <= 0:
         print("Invalid floor.")
         sys.stdout.flush()
         return(elevator_number, current_floor, requested_floor)
    elif current_floor == requested_floor:
        print("Elevator:[{}]{}|{}".format(elevator_number, current_floor, requested_floor))
        sys.stdout.flush()
        return(elevator_number, current_floor, requested_floor)

    if requested_floor > current_floor:
        elevator_string = "{}{}{}".format(current_floor, (">" * requested_floor), requested_floor)
    else:
        elevator_string = "{}{}{}".format(requested_floor, ("<" * requested_floor), current_floor)

    print("Elevator[{}]{}".format(elevator_number,elevator_string ))
    sys.stdout.flush()

    return(elevator_number, current_floor, requested_floor)

if __name__ == '__main__':
    with Pool(5) as p:
        elevators = [(0,1,1), (1,1,1), (2,1,1)]
        p.map(f, elevators)

        while True:
            try:
                elevator = int(input("Elevator?:"))
                new_floor = int(input("Floor?:"))
                if elevator < 0 or elevator > (len(elevators) -1):
                    raise
                if new_floor < 0 :
                    raise

                tmp1, current_floor, tmp2 = elevators[elevator]
                elevators[elevator] = (elevator, current_floor, new_floor)
                p.map(f, elevators)
                elevators[elevator] = (elevator, new_floor, new_floor)
            except :
                print("invalid input")
                exit(0)

