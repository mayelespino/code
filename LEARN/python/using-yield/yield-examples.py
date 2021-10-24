#!/usr/local/bin/python3

def yieldFibbunacci(number):
    """
    generate a fibunnaci series
    :param number:
    :return:
    """
    fibb, prev = 0,1
    for x in xrange(number):
        fibb, prev = fibb+prev, fibb
        if x > 0:
            yield fibb
#
#
#
def main():
    print("Main")
    for fibb in yieldFibbunacci(10):
        print(fibb)
#
#
#
if __name__ == "__main__" : main()