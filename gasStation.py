from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # sanity check that we have enough gas to cover costs
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        
        """
        Compute the difference between gas and cost.
        diff[i] being negative indicates that we can't start at that 
        gas station i as we don't have enough gas to travel to the next
        station.
        """
        diff = [gas[i] - cost[i] for i in range(n)]

        """
        Iterate over the diff array and maintain a running total. In each iteration
        we add the diff value, if adding the diff makes the running total negative
        we reset the total to 0 and record this index in idx to note the last index
        that caused the total to reset. As we are guranteed to have a solution, (we 
        already checked that sum(gas) >= sum(cost)) idx + 1 would indicate the idx 
        from where we can start a successful circuit
        """
        idx, total = -1, 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total, idx = 0, i
        return (idx + 1) % n
    
soln = Solution()
assert soln.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]) == 3
assert soln.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]) == -1