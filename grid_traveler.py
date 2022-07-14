import time

def grid_traveler(n,m):
 
    if n == 1 and m == 1:
         return 1
    if n == 0 or m == 0:
         return 0

    return grid_traveler(n - 1, m) + grid_traveler(n, m - 1)

def grid_traveler_memoied(n,m, memo={}):
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

    memo[key] = grid_traveler_memoied(n - 1, m, memo) + grid_traveler_memoied(n, m - 1, memo)
    memo[ikey] = memo[key]
    return memo[key]

start_time = time.time()

print(grid_traveler(0,1))
print(grid_traveler(1,1))
print(grid_traveler(4,6))
print(grid_traveler(13,14))

print("Run took", time.time() - start_time, "seconds")

start_time = time.time()

print(grid_traveler_memoied(0,1))
print(grid_traveler_memoied(1,1))
print(grid_traveler_memoied(4,6))
print(grid_traveler_memoied(13,14))

print("Run took", time.time() - start_time, "seconds")