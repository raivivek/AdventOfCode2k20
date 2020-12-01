nums = [int(x.strip()) for x in open("input", "r").readlines()]
target_sum = 2020

# Part 1
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            print("Part 1:", nums[i] * nums[j])

# Part 2
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if (target_sum - nums[i] - nums[j]) in nums[j:]:
            print("Part 2:", nums[i] * nums[j] * (target_sum - nums[i] - nums[j]))
