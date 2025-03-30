
class Solution:
    def threeSum(self, nums):
        result = []
        n = len(nums)
        
        if n < 3:
            return result

        nums.sort()  # Sort the array for two-pointer technique

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
                continue
            
            left = i + 1
            right = n - 1
            target = -nums[i]

            while left < right:
                sum = nums[left] + nums[right]
                
                if sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    print(f"Found: {nums[i]},{nums[left]},{nums[right]}")
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result

def print_vector(vec):
    print("[", end="")
    for i in range(len(vec)):
        print("[", end="")
        for j in range(len(vec[i])):
            print(vec[i][j], end="")
            if j < len(vec[i]) - 1:
                print(",", end="")
        print("]", end="")
        if i < len(vec) - 1:
            print(",", end="")
    print("]")

def test(nums, expected):
    solution = Solution()
    result = solution.threeSum(nums)
    
    result.sort()
    expected.sort()

    passed = result == expected
    
    print("Input: ")
    print_vector([nums])
    
    print("Output: ")
    print_vector(result)
    
    print("Expected: ")
    print_vector(expected)
    
    print("✅ Test Passed!" if passed else "❌ Test Failed!")
    print("---------------------------------------------")
    return passed

    if __name__ == "__main__":
    all_passed = True
    
    all_passed &= test([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    all_passed &= test([0, 1, 1], [])
    all_passed &= test([0, 0, 0], [[0, 0, 0]])
    all_passed &= test([-4, -1, -1, 0, 1, 2], [[-4, 1, 2], [-1, -1, 2], [-1, 0, 1]])
    all_passed &= test([1, -1], [])
    all_passed &= test([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 
                       [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]])
    all_passed &= test([0, 0, 0, 0, 0, 0], [[0, 0, 0]])
    all_passed &= test([-5, -3, -1, -2, -4], [])
    all_passed &= test([1, 2, 3, 4, 5], [])
    all_passed &= test([-2, 0, 2, -2, 1, 1], [[-2, 0, 2], [-2, 1, 1]])
    all_passed &= test([-4, -1, -1, 0, 1, 2, 3], [[-4, 1, 3], [-1, -1, 2], [-1, 0, 1]])

    if all_passed:
        print("🎉 All test cases passed successfully! 🎉")
    else:
        print("❌ Some test cases failed. Please check the failed cases!")
