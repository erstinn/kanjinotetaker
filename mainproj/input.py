from pathlib import Path
import shelve
import pprint
import os

# # import os
# # full_path = os.path.realpath(__file__)
# # print(full_path + "\n")
#
# import os
# from pathlib import Path
#
#
# # Path.cwd()
# # os.chdir('/home/ahiru/Documents')
# # Path.cwd()
# # Path(jpn.__file__).parent.absolute()
#
# # #if txt does not exist: ask for default; should be fixed path:inside py file's folder
# # if Pathnotfound: prompt path; set path as default
#
# # #if to get file from user:
# # #input1 = input()
# # #Path (input1)
# # Path('home', 'ahiru', 'cute')
# # tags = input()
# # kanji = input()
# # word_list = {}
# # word_list[tags] = kanji
#
# # print(__file__)/


class KanjiNoteTaker:
    kanji_dictionary = {
        'Tag': [], 'Kanji': [], 'Meaning': []
    }

    def __int__(self):
        # read from a text file, if empty, break from reading the text
        if os.path.isfile('kanji_shelf'): # check if file exists
            kanji_dictionary = shelve.open('kanji_shelf')
        else:
            kanji_shelf = shelve.open('kanji_shelf')
            kanji_shelf['dictionary'] =

        kanji_shelf['kanjilist'] =


    def take_input(self):
        error_input = 1

        while error_input == 1:
            print("[C]ommon/[U]ncommon/[n1]/[n2]/[n3]/[n4]/[n5] (ex:cn1 or UN5)")
            print("\nInput separated by a '-' ex: UN4 - 漢字(かんじ) - MEANING")
            print("\n[INPUT]: ")
            kanji_input = input().lower()
            kanji = [x.strip() for x in kanji_input.split('-')]
            if len(kanji) < 3:
                print("need complete input")
                kanji.clear()
                continue
            else:
                error_input = 0
                kanji_dict(kanji[0], kanji[1], kanji[2])

    def tag_options(self, tag):
        # how to even convert it to something efficient lol;changesomeday perhaps mayev
        final_tag = ""
        tag = list(tag)
        if not tag:  # simply checks if empty input; should i change or add an or
            print("Invalid tag")
            return
        for x in tag:
            if x == 'c':
                final_tag = "Common"
                continue
            elif x == 'u':
                final_tag = "Uncommon"
                continue
            elif x == 'n':
                if tag[0] == 'c' or tag[0] == 'u':  # if it already has common/uncommon
                    final_tag = final_tag + ', N' + tag[2]
                    return final_tag
                else:
                    final_tag = 'N' + tag[1]
                    return final_tag
            else:
                print("Wrong input, try again")
                tag = input().lower()
                tag_options(tag)
                break

        return final_tag

    def kanji_dict(self, tag, kanji, meaning):
        get_tag = self.tag_options(self, tag)





# verbose; list all of the data; efficiency later
# can/should only be used when needed: debugging; checking, etc.
# def listAll():
#     for i in kanji.items():
#         print(i)

if __name__ == '__main__':
    take_input()
