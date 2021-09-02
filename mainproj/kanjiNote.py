from pathlib import Path
import csv
import pyinputplus as pyinp
import os
import sys


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

    def __int__(self):
        self.kanji_dictionary = {  # automatically static; I think
            'word': {'reading': '', 'tag': '', 'type': '', 'meaning': '', 'proficiency': ''}
        }

        if os.path.isfile('kanji.csv') and os.path.getsize('kanji.csv'):
            kanji_csv = open('kanji.csv')
            kanji_reader = csv.DictReader(kanji_csv, ['word', 'reading', 'tag', 'type', 'meaning', 'proficiency'])

            # put csv contents into the dictionary where the unique key of the outer dictionary
            # is the kanji in the csv
            for row in kanji_reader:
                self.kanji_dictionary[row['word']]['reading'] = row['reading']
                self.kanji_dictionary[row['word']]['tag'] = row['tag']
                self.kanji_dictionary[row['word']]['type'] = row['type']
                self.kanji_dictionary[row['word']]['meaning'] = row['meaning']
                self.kanji_dictionary[row['word']]['proficiency'] = row['proficiency']

    def takeinput(self):
        continue_input = 'y'
        kanji_list = []
        while continue_input == 'y':
            try:
                tag = pyinp.inputStr(prompt="[C]ommon/[U]ncommon/[n1]/[n2]/[n3]/[n4]/[n5] (ex:cn1) \n[TAG]:",
                                     blank=True,
                                     allowRegexes='cu|[n][1-5]|[cu][n][1-5]|[n][1-5][')
                kanji = input("[KANJI]:")
                tag = input().lower()
                typ = pyinp.inputStr(prompt="(ex:noun) [TYPE]:", blank=True)
                hiragana = pyinp.inputStr(prompt="[READING]:", blank=True)
                meaning = input("[MEANING]:")
                proficiency = pyinp.inputChoice(['low', 'high', 'normal'], blank=True)

                self.kanji_dictionary[kanji] = {'reading': hiragana,
                                                'tag': tag,
                                                'type': typ,
                                                'meaning': meaning,
                                                'proficiency': proficiency}
                self.kanjicsv(self.kanji_dictionary)
                self.kanji_dictionary.clear()

                continue_input = pyinp.inputChoice(['y', 'n'], prompt="\nInput again?", caseSensitive=False, blank=True)
                if continue_input == '':
                    continue_input = 'y'

            except Exception as e:
                print(e)

    def tagoptions(self, tag):
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
                self.tagoptions(tag)
                break

        return final_tag

    def kanjicsv(self, kanji_dictionary):

        # tag, type, kanji, hiragana, meaning, proficiency as index of dictionary
        tag = self.tagoptions(kanji_dictionary)

        kanji_csv = open('kanji.csv', 'w')
        write_kanji = csv.DictWriter(kanji_csv,
                                     fieldnames=['word', 'reading', 'tag', 'type', 'meaning', 'proficiency'])
        write_kanji.writeheader()
        write_kanji.writerow({'word': {self.kanji_dictionary['word']},
                              'reading': {self.kanji_dictionary['reading']},
                              'tag': {self.kanji_dictionary['tag']},
                              'type': {self.kanji_dictionary['type']},
                              'meaning': {self.kanji_dictionary['meaning']},
                              'proficiency': {self.kanji_dictionary['proficiency']}})
