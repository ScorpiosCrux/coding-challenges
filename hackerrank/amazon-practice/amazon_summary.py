from operator import itemgetter

#input arr
arr = [2,1,2,2]

#Parse the arr for freq
parsed_arry = [[0 for x in range(2)] for y in range(len(arr))]
for x in arr:
    parsed_arry[x][1] += 1
    parsed_arry[x][0] = x

#Sort the array by 2nd column from desc order.
sorted_arr = sorted(parsed_arry, key=itemgetter(1), reverse=True)

#Count how many rows we need in the array
count = 0
for line in sorted_arr:
    if line[0] != 0:
        count += 1

#Copy the sorted array with extra rows over to the array with no extra zeros to match the stdout
finished_arr = [[0 for x in range(2)] for y in range(count)]
for i in range(len(sorted_arr)):
    if sorted_arr[i][0] == 0:
        break
    else:
        finished_arr[i] = sorted_arr[i]





