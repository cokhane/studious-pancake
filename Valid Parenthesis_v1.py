'''

Valid Parenthesis

startdate: 070125

'''

class Solution:

    def find_i_pair(self, index, value, pair):
        print("inside find pair method")
        print(f"index: {index}, value: {value}, pair: {pair}")
        for i in pair:
            if i["value"] == value and i["index"] == index:
                return True

        return False

    def check_value_if_exist_in_find_pair(self, value, find_pair):
        for i in find_pair:
            if i["value"] == value:
                return True

        return False

    def isValid(self, s: str) -> str:
        char_list = s

        starting_list = '([{'
        tail_list = ')]}'
        done_pairing = []

        find_pair = []
        skip_now = False
        i = 0
        outer_loop = True

        if len(s) == 1:
            return False

        print("problem!: ",s)

        while i < 100:
        # while outer_loop:
            print('START OUTER LOOP')
            print('find_pair: ', find_pair)
            print('char_list: ', char_list)
            print('---------------------------------')
            for index,j in enumerate(char_list):
                print('---------------------------------')
                print('START INNER LOOP', index, j)
                find_done_pairing_value = [x for x in done_pairing if x["value"] == j and x["index"]==index]
                print('find_done_pairing_value: ', find_done_pairing_value)

                for k in done_pairing:
                    print('inside done pairing loop')
                    print("k val" ,k["value"], "k index" ,k["index"])
                    print("j val",j, "j index",index)
                    if k["value"] == j and k["index"] == index:
                        print("found skipping: ", k)
                        skip_now = True
                        break

                    if k["value"] == j:
                        find_tail_list = tail_list[int(starting_list.find(j))]
                        print('its a tail ', find_tail_list)
                        if find_tail_list == j:
                            return False

                find_pair_condition = self.find_i_pair(index, j, find_pair)

                print('find_pair_condition: ', find_pair_condition)

                if find_pair_condition or skip_now:
                        print('INSIDE SKIP CONDITION')
                        print('SKIP THIS ', j)
                        skip_now = False
                        if len(done_pairing) + len(find_pair) == len(char_list):
                            return False
                        continue

                if starting_list.find(j) > -1:
                    print('---------------------------------')
                    print('INSIDE FIND PAIR CONDITION', j)

                    does_value_exist_in_find_pair = self.check_value_if_exist_in_find_pair(j,find_pair)

                    print("does_value_exist_in_find_pair: ", does_value_exist_in_find_pair)
                    print('j: ', j)
                    print('index: ', index)

                    if does_value_exist_in_find_pair:
                        return False

                    if len(find_done_pairing_value) == 0 and not does_value_exist_in_find_pair:
                        print('---------------------------------')
                        print('-------- inside does_value_exist_in_find_pair FALSE')
                        print('j: ', j)
                        print('index: ', index)

                        new_dict = { "index": index, "value": j}

                        print("new_dict: ", new_dict)
                        print('---------------------------------')
                        find_pair.append(new_dict)
                    print('---------------------------------')
                    print('FIND PAIR UPDATED 50: ', find_pair)
                    print('---------------------------------')
                    print('BREAK THE INNER LOOP')
                    print('---------------------------------')
                    break

                else:
                    # if len(done_pairing) > 0 and len(find_pair) == 0 or len(find_pair) == 0 and tail_list.find(j) > -1:
                    if len(find_pair) == 0:
                        print("Cannot find starting list", j)
                        return False


                if len(find_pair) > 0:
                    print('INSIDE FIND TAIL CONDITION')
                    find_pair_last_element = find_pair[-1]["value"]
                    find_pair_last_element_index = find_pair[-1]["index"]

                    find_tail_list = tail_list[int(starting_list.find(find_pair_last_element))]

                    print('find_tail_list: ', find_tail_list)
                    print('j: ',  j)
                    print('index: ',  index)

                    if  find_tail_list == j:
                        print('its a pair')
                        new_dict = { "index": find_pair_last_element_index, "value": find_pair_last_element}
                        done_pairing.append(new_dict)
                        new_dict_tail =  { "index": index , "value": j}
                        done_pairing.append(new_dict_tail)

                        char_list.pop(j)

                        if len(done_pairing) == len(s):
                            print('done_pairing: ', done_pairing)
                            return True

                        print('---------------------------------')
                        print('find_pair befor pop', find_pair)
                        print('---------------------------------')
                        find_pair.pop()

                        print('---------------------------------')
                        print('find_pair now', find_pair)
                        print('break!')
                        print('---------------------------------')
                        break
                    else:
                        return False
            i = i + 1
            if len(find_pair) == len(char_list):
                print('---------------------------------')
                print("FIND PAIR == CHAR LIST")
                return False
        return True

axe = Solution()

# print('----------FINAL OUTPUT: ',axe.isValid('()'))
# print('----------FINAL OUTPUT: ',axe.isValid('()[]'))
# print('----------FINAL OUTPUT: ',axe.isValid('()[]{}'))
# print('----------FINAL OUTPUT: ',axe.isValid('([])'))
print('----------FINAL OUTPUT: ',axe.isValid('(([]){})'))



#FIXING
#FALSE
# print('----------FINAL OUTPUT: ',axe.isValid("([)]"))
# print('----------FINAL OUTPUT: ',axe.isValid("(){}}{"))
# print('----------FINAL OUTPUT: ',axe.isValid("(}{)"))
# print('----------FINAL OUTPUT: ',axe.isValid("({{{{}}}))"))
# print('----------FINAL OUTPUT: ',axe.isValid('(]'))
# print('----------FINAL OUTPUT: ',axe.isValid('['))
# print('----------FINAL OUTPUT: ',axe.isValid('(('))
# print('----------FINAL OUTPUT: ',axe.isValid('(['))
# print('----------FINAL OUTPUT: ',axe.isValid("([]){"))
# print('----------FINAL OUTPUT: ',axe.isValid("([]){"))
# print('----------FINAL OUTPUT: ',axe.isValid("[])"))
# print('----------FINAL OUTPUT: ',axe.isValid("]["))






# print('----------FINAL OUTPUT: ',axe.isValid(']'))

# print('axe: ',axe.axe_test())