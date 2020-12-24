#code {1421A - 23}
import sys

def xorWise():
    t = int(input())  # tesecase
    while t > 0 :

      first,second = map(int,sys.stdin.readline().split())

      x = first & second        #  X should be & value of A and B.
      sum = (first^x) + (second^x)
      print(sum)
      t = t - 1 ;

xorWise()
