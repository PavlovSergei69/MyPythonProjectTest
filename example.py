candies = [2,3,5,1,3]
extraCandies = 3
result = []
if extraCandies+candies[0]>=max(candies):
    result.append(True)
else:
    result.append(False)

if extraCandies+candies[1]>=max(candies):
    result.append(True)
else:
    result.append(False)

if extraCandies + candies[2] >= max(candies):
    result.append(True)
else:
    result.append(False)

if extraCandies+candies[3]>=max(candies):
    result.append(True)
else:
    result.append(False)

if extraCandies + candies[4] >= max(candies):
    result.append(True)
else:
    result.append(False)
print(result)

