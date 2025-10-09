'''

CURRENT SITUATION AND PROBLEM

so the problem is

ab, a

len(first_word) == len(matching)

items = 1

same problem with flower -.-

'''

from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = [i for i in strs if i == '']
        if x:
            return ""

        if len(strs) == 1:
            return strs[0]

        get_first_word = strs[0]
        matching_words = get_first_word[0]
        was_there_a_match = False
        destroy = False
        match_count = 0
        total_array_length = len(strs)
        index_tracker = 0
        limiter = 0
        mis_match = 0
        last_match = ''
        # while destroy is False:
        i = 0
        while not destroy:
        # while i < 10:
            match_count = 0

            for items in range(len(strs)):
                    iterate_word = strs[items]
                    to_match = iterate_word[0:int(len(matching_words))]
                    if matching_words == to_match:
                        match_count += 1
                    else:
                        matching_words = last_match
                        destroy = True
                        break


                    if match_count == total_array_length:
                        was_there_a_match = True

                        if (index_tracker + 1) < len(get_first_word):
                            index_tracker = index_tracker + 1
                            last_match = matching_words

                            matching_words = matching_words + get_first_word[index_tracker]
                        else:
                            destroy = True

                            break

                    if len(matching_words) == len(get_first_word) and items == total_array_length:
                        destroy = True
                        if match_count != total_array_length:
                            matching_words = last_match
                        break

        return matching_words if was_there_a_match else ""

test = Solution()


'''

supafast solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        strs_length = len(strs[0])
        if len(strs) == 1:
            return strs[0]
        for i in range(strs_length):
            for_check = strs[0][:(strs_length-i)]
            is_good = all(s.startswith(for_check) for s in strs)
            if is_good:
                return for_check
        return ""


'''



# print('-----------FINALE ANSWERRR ',test.longestCommonPrefix(["flower","flow","flight"]))
# print('-----------FINALE ANSWERRR ',test.longestCommonPrefix(["c","acc","ccc"]))

# print('-----------FINALE ANSWERRR ',test.longestCommonPrefix(["dog","racecar","car"]))
# print('-----------FINALE ANSWERRR ',test.longestCommonPrefix(["a"]))
# print('-----------FINALE ANSWERRR ',test.longestCommonPrefix(["cir","car"]))

# print('-----------FINALE ANSWERRR: ',test.longestCommonPrefix(["ab","a"]))
# print('-----------FINALE ANSWERRR: ',test.longestCommonPrefix(["flower","flower","flower","flower"]))

# print(test.longestCommonPrefix([""]))
