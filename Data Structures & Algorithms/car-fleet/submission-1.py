class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        n = len(position)

        car = sorted(zip(position, speed), reverse=True)
        
        for pos, spd in car:
            dist = target - pos
            time = dist / spd

            if not st or time > st[-1]:
                st.append(time)

        return len(st)
