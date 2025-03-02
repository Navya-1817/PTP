n = int(input())
arr = list(map(int, input().split()))

arr.sort()

maxxo = arr[-1]
sec_max = None
for i in range(n-2, -1, -1):
    if arr[i] != maxxo:
        sec_max = arr[i]
        break

if sec_max is not None:
    print(sec_max)
else:
    print("No second largest element")