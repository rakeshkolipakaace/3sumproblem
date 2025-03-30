#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    public:
     vector<vector<int>> threeSum(vector<int>& nums) {
             vector<vector<int>> result;
            int n = nums.size();
            
            if (n < 3) return result; // Not enough elements
            
            sort(nums.begin(), nums.end()); // Step 1: Sort the array
            
            for (int i = 0; i < n - 2; i++) {
                if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicates for i
                
                int left = i + 1, right = n - 1;
                int target = -nums[i];
                
                while (left < right) {
                    int sum = nums[left] + nums[right];
                    
                    if (sum == target) {
                        result.push_back({nums[i], nums[left], nums[right]});
                        
                        // Move left and right pointers, skipping duplicates
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        
                        left++;
                        right--;
                    } 
                    else if (sum < target) {
                        left++; // Increase sum
                    } 
                    else {
                        right--; // Decrease sum
                    }
                }
            }
            return result;
          
        }
    };