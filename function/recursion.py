# maximun recursion limit is 1000, by default 
import sys
print(sys.getrecursionlimit())

# setting the new limit for the recursion 
sys.setrecursionlimit(20000)

print(sys.getrecursionlimit())