import csv
from pynput.keyboard import Controller, Key
import time
import os


class Word:
    def __init__(self):
        self.keyboard = Controller()

    def readFile(self):
        # Read the word list from the file
        with open("./word-liste.csv", 'r', encoding='utf-8') as file_csv:
            csvreader = csv.reader(file_csv, delimiter=",")
            dic = {}
            for ligne in csvreader:
                key = ligne[0].strip()
                value = ligne[1].strip()

                # Capitalize the first letter if it is lowercase
                if key[0].islower():
                    key = key[0].upper() + key[1:]

                if value[0].islower():
                    value = value[0].upper() + value[1:]

                dic[key] = value

            return dic

    def sortDict(self, dic):
        # Sort the dictionary by keys in alphabetical order
        myKeys = sorted(dic.keys())
        dic = {key: dic[key] for key in myKeys}

    def formatWordList(self, dic):
        # Write the formatted word list to a new CSV file
        with open("./word-listeUpdated.csv", 'w', newline='', encoding='utf-8') as file_csv:
            csvwriter = csv.writer(file_csv)
            csvwriter.writerows(dic.items())

    def writeWordAnki(self):
        wordDict = {}
        # Read the formatted word list from the file
        with open("./word-listeUpdated.csv", 'r', encoding='utf-8') as file_csv:
            csvreader = csv.reader(file_csv, delimiter=",")
            for line in csvreader:
                key = line[0]
                value = line[1]
                wordDict[key] = value

        # Write the words to Anki using keyboard input
        for key, value in wordDict.items():
            self.keyboard.type(key)
            time.sleep(0.3)
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)
            time.sleep(0.3)
            self.keyboard.type(value)
            time.sleep(0.3)
            self.keyboard.press(Key.ctrl)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            self.keyboard.release(Key.ctrl)
            time.sleep(0.3)


    def addWordToFullListe(self, dic):
        with open("./FullListe.csv", 'a', newline='', encoding='utf-8') as file_csv:
            csvwriter = csv.writer(file_csv)
            for key, value in dic.items():
                csvwriter.writerow([key, value])

        # Sort the full word list by alphabetical order
        with open("./FullListe.csv", 'r', encoding='utf-8') as file_csv:
            lines = file_csv.readlines()
            lines.sort(key=lambda line: line.split(',')[0].strip())

        with open("./FullListe.csv", 'w', newline='', encoding='utf-8') as file_csv:
            file_csv.writelines(lines)


def menu():
    os.system('cls')
    print("1. Format File")
    print("2. Write word to Anki")
    print("3. Add new word to the full word list")
    print("4. Exit")

    choice = input("Choose an option: ")

    return menu() if choice not in ["1", "2", "3", "4"] else int(choice)


def main():
    word = Word()
    choice = menu()

    if choice == 1:
        wordDict = word.readFile()
        word.sortDict(wordDict)
        word.formatWordList(wordDict)
        main()

    elif choice == 2:
        for i in range(3, 0, -1):
            print(f"...{i}")
            time.sleep(1)
        word.writeWordAnki()

    elif choice == 3:
        wordDict = word.readFile()
        word.addWordToFullListe(wordDict)
        main()


if __name__ == '__main__':
    main()
