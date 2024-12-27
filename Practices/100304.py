from typing import List
from collections import defaultdict

class Solution:
    def maxDamage(self, power: List[int]) -> int:
        # Sort the power array
        power.sort()
        
        # Dictionary to keep track of the maximum damage for each power
        damage_dict = defaultdict(int)
        
        # Iterate through the sorted power array
        for p in power:
            # Update the maximum damage for current power
            damage_dict[p] = max(damage_dict[p], damage_dict[p-3] + p, damage_dict[p-4] + p)
        
        # Return the maximum damage from the dictionary
        return max(damage_dict.values())

# Example usage
solution = Solution()
print(solution.maxDamage([1, 1, 3, 4]))  # Output: 6
print(solution.maxDamage([7, 1, 6, 6]))  # Output: 13


# Example usage
solution = Solution()
print(solution.maxDamage([1, 1, 3, 4]))  # Output: 6
print(solution.maxDamage([7, 1, 6, 6]))  # Output: 13

