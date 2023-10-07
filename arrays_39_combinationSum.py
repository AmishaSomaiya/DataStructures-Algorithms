"""
https://leetcode.com/problems/combination-sum/
https://la60312.medium.com/leetcode-39-combination-sum-79df7114879a#:~:text=LeetCode%20%2339%2C%20Combination%20Sum%2C,combination%20equals%20to%20the%20target.

leetcode 
medium
arrays, backtracking 

input : an array of distinct integers candidates and a target integer target
output: a list of all unique combinations of candidates where the chosen numbers 
sum to target

Explanation: The algorithm is simple; just use backtracking techniques. 
Note that we use variable index to avoid duplicated combination. So, whenever index becomes 
larger, we cannot choose number before the index element in candidates array.

Time Complexity: O(2^k), where k is the number of tree nodes of the recursion tree. 
In this given problem, k is the sum of target/candidates[i] from i=0 to len(candidates)-1.

Space Complexity: O(n), where n is the length of longest combination. 
In worst case scenario, N = target when 1 is in the candidates array.

"""

def combinationSum(candidates, target):
    def find_all_combination(index, target, path):
        if target < 0:
            return
        elif target == 0:
            output_list.append(path)
        else:
            for i in range(index, cand_length):
                find_all_combination(i, target-cand[i], path+[cand[i]])
        return

    output_list = []
    cand = candidates
    cand_length = len(candidates)
    find_all_combination(0, target, [])

    return output_list

print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))