#code {}
import math

def main():

    x = int(input()) #x Bacteria
    count  = 0 ;

    while x/2 > 0 :
        if ( x % 2 == 1 ):
            count = count + 1

        x = int(x / 2)

    print(count)


main()
