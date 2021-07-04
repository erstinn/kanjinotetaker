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


def take_input():
    print("[C]ommon/[U]ncommon/[n1]/[n2]/[n3]/[n4]/[n5] (ex:cn1 or UN5)")
    tag = input().lower()
    print("\n言葉: ")
    kanji = input()
    kanji_dict(tag, kanji)


def tag_options(tag):
    # how to even convert it to something efficient lol;changesomeday perhaps mayev
    final_tag = ""
    tag = list(tag)
    if not tag:
        print("Invalid input, try again")
        return
    for x in tag:
        if x == 'c':
            final_tag = "Common"
            continue
        elif x == 'u':
            final_tag = "Uncommon"
            continue
        elif x == 'n':
            final_tag = 'N' + tag[3]
            if tag[0] == 'c' or 'u':
                final_tag = final_tag + ', N' + tag[2]
        else:
            print("Wrong input, try again")

    return final_tag


def kanji_dict(tag, kanji):
    tag_options(tag)
    if tag == "":
        print("\nTry Again")
        tag_options(tag)


# verbose; list all of the data; efficiency later
# can/should only be used when needed: debugging; checking, etc.
# def listAll():
#     for i in kanji.items():
#         print(i)

if __name__ == '__main__':
    take_input()
