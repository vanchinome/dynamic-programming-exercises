import time

def grid_traveler_best(n,m, memo={}):
    key = f"{n}-{m}"
    ikey = f"{m}-{n}"
    if  key in memo:
        return memo[key]
    if  ikey in memo:
        return memo[ikey]
    if n == 1 and m == 1:
         return 1
    if n == 0 or m == 0:
         return 0

    memo[key] = grid_traveler_best(n - 1, m, memo) + grid_traveler_best(n, m - 1, memo)
    memo[ikey] = memo[key]
    return memo[key]

def grid_traveler(n,m):
 
    if n == 1 and m == 1:
         return 1
    if n == 0 or m == 0:
         return 0

    return grid_traveler(n - 1, m) + grid_traveler(n, m - 1)

start_time = time.time()

print(grid_traveler(0,1))
print(grid_traveler(1,1))
print(grid_traveler(2,3))
print(grid_traveler(13,13))

print(time.time() - start_time, "seconds")

start_time = time.time()

print(grid_traveler_best(0,1))
print(grid_traveler_best(1,1))
print(grid_traveler_best(2,3))
print(grid_traveler_best(13,13))

print(time.time() - start_time, "seconds")