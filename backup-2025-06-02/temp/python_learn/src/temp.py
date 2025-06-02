# Edit the function provided by calling partial()
#       and replacing the first three variables in func().
# Then print with the new partial function using
#       only one input variable so that the output equals 60.
list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    index = 0
    i = 0
    while i < len(nums):
        count = nums.count(nums[index])
        if count >= 1:
            print("count: ", count)
            i += count
            index += 1
            if i >= len(nums):
                break
            print("--------------------------------")
            print("i: ", i, nums[i])
            print("index: ", index, nums[index])
            nums[index] = nums[i]
            i -= 1
            print(nums)
            print("--------------------------------")
        else:
            i += 1
            index += 1
            print("================================")
            print("i: ", i)
            print("index: ", index)
            print("================================")

    return index


if __name__ == '__main__':
    print("testing")
    a = removeDuplicates(list)
    print(list[:a])
