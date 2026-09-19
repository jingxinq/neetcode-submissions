class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #car can only form a fleet with the one in front of it
        #only if the car ahead has a time greater than or equal to the time behind aka slower
        #maintain total num of fleet through a stack in DESCENDING ORDER?
        #why descending order

        # if can join the fleet, dont push
        #if cannot join the fleet, push

        pairs = list(zip(position, speed))
        pairs.sort(key=lambda pair:pair[0], reverse=True)

        stack = []
        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            if not stack:
                stack.append(time)
            elif time > stack[-1]: # take longer
                stack.append(time)
            
        return len(stack)
                
            

