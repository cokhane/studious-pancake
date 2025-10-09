class Solution:
    def remove_string_on_substring(self,s: str, list):

        print(s.replace(s[2],""))
        new_string = s.replace(s[2],"")
        print(new_string.replace(new_string[2],""))
        # print(s.replace(s[],""))
        return s



test = Solution()

print('new string',test.remove_string_on_substring('(([]){})',[{'index': 2, 'value': '['}, {'index': 3, 'value': ']'}]))
