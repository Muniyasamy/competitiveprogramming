#code {HW2E}

import sys

def maximumNonDecreasingOrder(n,arr):
    max = int(0)
    sum = int(0)
    for i in range(1,n):
      if ( arr[i-1] <= arr[i] ) :
          sum = sum + 1
      else:
         sum = 0

      if sum >= max :
        max = sum

    return ( max + 1 ) if max > 0 else 0 


def main():

    n = int(input()) ;
    arr = list(map(int,sys.stdin.readline().split(' ')[:n]))
    print(maximumNonDecreasingOrder(n,arr))

main()
