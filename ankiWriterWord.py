import csv
from pynput.keyboard import Controller
from pynput.keyboard import Key
import time

keyboard = Controller()

wordDict = {}

time.sleep(5)

with open("./wordUpdated.csv", 'r', encoding='utf-8') as file_csv:
    csvreader = csv.reader(file_csv, delimiter=",")
    for line in csvreader:
        key = line[0]
        value = line[1]
        wordDict[key] = value

for key, value in wordDict.items():
    print(f"{key} : {value}")

for key, value in wordDict.items():
    keyboard.type(key)
    time.sleep(0.3)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(0.3)
    keyboard.type(value)
    time.sleep(0.3)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.release(Key.ctrl)
    time.sleep(0.3)