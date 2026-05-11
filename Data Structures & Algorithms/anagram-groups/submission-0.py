class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hash_map = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            hash_map[sorted_str].append(s)
        return list(hash_map.values())
        O(n*klogk) - n = number of strings, k - length of each string, logk - sorting string of length k
        """
        hash_map = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a...z
            for char in s:
                count[ord(char) - ord('a')] += 1
            hash_map[tuple(count)].append(s)
        return list(hash_map.values())

        # O(n*k) - no sorting, just counting chars.


