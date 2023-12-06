import math

# part 1 should output 6209190
print("part 1")
print(
    math.prod(
        sum(i * (limit - i) > dist for i in range(dist))
        for limit, dist in zip([40, 92, 97, 90], [215, 1064, 1505, 1100])
    )
)

# part 2 should output 28545089, it did take about 23 sec to 
# process because this is not optimized in any way
print("part 2")
limit, dist = 40929790, 215106415051100
print(sum(i * (limit - i) > dist for i in range(limit)))

# why was this so easy 😭