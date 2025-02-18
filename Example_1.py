# candies = [2,3,5,1,3]
# extraCandies = 3
# result = []
# for extraCandies in candies:
#     if extraCandies+candies[] in candies:
#         print(True)

candies = [2,3,5,1,3]
extraCandies = 3
result = []
for a in candies:
    if extraCandies + a >= max(candies):
        result.append(True)
    else:
        result.append(False)