from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        groups = defaultdict(list)

        for word in strs:

            # Sắp xếp chuỗi làm key
            key = ''.join(sorted(word))

            groups[key].append(word)

        return list(groups.values())