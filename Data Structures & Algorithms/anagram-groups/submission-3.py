class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freq_map = {}

        for s in strs:
            array = [0] * 26
            for char in s:
                char_pos = ord(char) - ord('a')
                array[char_pos] += 1

            if tuple(array) in freq_map:
                freq_map[tuple(array)].append(s)
            else:
                freq_map[tuple(array)] = [s]

        return list(freq_map.values())

