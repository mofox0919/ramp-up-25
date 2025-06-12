def lcm(nums):
    if len(nums) == 1:
        return nums[0]
    m = 1
    for num in nums:
        m *= num
    return m // gcd(nums)

def gcd(nums):
    if len(nums) == 1:
        return nums[0]
    g = nums[0]
    for num in nums[1:]:
        while num != 0:
            g, num = num, g % num
    return g

def main():
	print(lcm([5]))

if __name__ == "__main__":
    main()

    