# def move(arr, k):
#   l, r, res, kRef = 0, 0, 0, k
#   while k > 0 and r < len(arr):
#     while arr[l] == 0:
#       l += 1
#     if arr[r] == 1:
#       kRef -= 1
#     if kRef != 0:
#       r += 1
#     else:
#       left_one_count, zero_count, count = 0, 0, 0
#       idx = l
#       while idx <= r:
#         while arr[idx] == 1 and idx <= r:
#           left_one_count += 1
#           idx += 1
#         else:
#           while arr[idx] == 0 and idx <= r:
#             zero_count += 1
#             idx += 1
#         if k - left_one_count > left_one_count:
#           count += left_one_count * zero_count
#         else:
#           count += (k - left_one_count) * zero_count
#         zero_count = 0
#       res = max(res, count)
#       print(res)

# print(move([0,0,1,0,0,1,0,1,1,0,0,0,0,1,0], 5))