import time

# checking performance of three ways
def odd_even_objects1(arr):
    oddcount = 0
    evencount = 0
    for obj in arr:
        if isinstance(obj, (list, tuple, set)):
            temp = odd_even_objects1(obj)
            oddcount += temp[0]
            evencount += temp[1]
        elif isinstance(obj, (int, float)):
            oddcount += obj % 2 != 0
            evencount += obj % 2 == 0

    return [oddcount, evencount]


def odd_even_count2(arr):
    oddcount = 0
    evencount = 0
    for obj in arr:
        if isinstance(obj, (list, tuple, set)):
            temp = odd_even_objects1(obj)
            oddcount += temp[0]
            evencount += temp[1]
        elif isinstance(obj, (int, float)):
            if obj % 2 == 0:
                evencount += 1
            else:
                oddcount += 1
    return [oddcount, evencount]

def odd_even_count3(arr):
    oddcount = 0
    evencount = 0
    for i in arr:
        if isinstance(i, (list, tuple, set)):
            temp = odd_even_objects1(i)
            oddcount += temp[0]
            evencount += temp[1]
        elif isinstance(i, int):
            if i & 1: 
                oddcount += 1
            else:
                evencount += 1
    return [oddcount, evencount]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11.234, 12.6]

start1 = time.time()
result1 = odd_even_objects1(arr)
end1 = time.time()

start2 = time.time()
result2 = odd_even_count2(arr)
end2 = time.time()

start3 = time.time()
result3 = odd_even_count3(arr)
end3 = time.time()

time1 = end1 - start1
time2 = end2 - start2
time3 = end3 - start3

def percentcount(t1, t2):
    if t1 == 0:
        return 0
    diff = ((t2 - t1) / time1) * 100
    return diff
diff2 = percentcount(time1, time2)
diff3 = percentcount(time1, time3)
print(f"time taken by approach 1: {time1} seconds")
print(f"time taken by approach 2: {time2} seconds ({'slower' if diff2 > 0 else 'faster'} by {abs(diff2)}%)")
print(f"time taken by approach 3: {time3} seconds ({'slower' if diff3 > 0 else 'faster'} by {abs(diff3)}%)")

