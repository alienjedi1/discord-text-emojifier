"""
Name: Lucas Patten
Project: Turn text into discord emotes
Date: 10/25/2020
"""
import time
import keyboard

def main():
    autoSend = False
    text = input("Input your text to turn into emojis here: ")
    time.sleep(3)
    utfList = list(text)
    i = 0
    for x in utfList:
        utfEmote = toEmoji(utfList[i])
        utfList[i] = utfEmote
        i += 1
    if autoSend == True:
        keyboard.press_and_release('enter')

def toEmoji(utfCharacter):
    if utfCharacter == "a" or utfCharacter == "A":
        keyboard.write(":regional_indicator_a: ")
    elif utfCharacter == "b" or utfCharacter == "B":
        keyboard.write(":regional_indicator_b: ")
    elif utfCharacter == "c" or utfCharacter == "C":
        keyboard.write(":regional_indicator_c: ")
    elif utfCharacter == "d" or utfCharacter == "D":
        keyboard.write(":regional_indicator_d: ")
    elif utfCharacter == "e" or utfCharacter == "E":
        keyboard.write(":regional_indicator_e: ")
    elif utfCharacter == "f" or utfCharacter == "F":
        keyboard.write(":regional_indicator_f: ")
    elif utfCharacter == "g" or utfCharacter == "G":
        keyboard.write(":regional_indicator_g: ")
    elif utfCharacter == "h" or utfCharacter == "H":
        keyboard.write(":regional_indicator_h: ")
    elif utfCharacter == "i" or utfCharacter == "I":
        keyboard.write(":regional_indicator_i: ")
    elif utfCharacter == "j" or utfCharacter == "J":
        keyboard.write(":regional_indicator_j: ")
    elif utfCharacter == "k" or utfCharacter == "K":
        keyboard.write(":regional_indicator_k: ")
    elif utfCharacter == "l" or utfCharacter == "L":
        keyboard.write(":regional_indicator_l: ")
    elif utfCharacter == "m" or utfCharacter == "M":
        keyboard.write(":regional_indicator_m: ")
    elif utfCharacter == "n" or utfCharacter == "N":
        keyboard.write(":regional_indicator_n: ")
    elif utfCharacter == "o" or utfCharacter == "O":
        keyboard.write(":regional_indicator_o: ")
    elif utfCharacter == "p" or utfCharacter == "P":
        keyboard.write(":regional_indicator_p: ")
    elif utfCharacter == "q" or utfCharacter == "Q":
        keyboard.write(":regional_indicator_q: ")
    elif utfCharacter == "r" or utfCharacter == "R":
        keyboard.write(":regional_indicator_r: ")
    elif utfCharacter == "s" or utfCharacter == "S":
        keyboard.write(":regional_indicator_s: ")
    elif utfCharacter == "t" or utfCharacter == "T":
        keyboard.write(":regional_indicator_t: ")
    elif utfCharacter == "u" or utfCharacter == "U":
        keyboard.write(":regional_indicator_u: ")
    elif utfCharacter == "v" or utfCharacter == "V":
        keyboard.write(":regional_indicator_v: ")
    elif utfCharacter == "w" or utfCharacter == "W":
        keyboard.write(":regional_indicator_w: ")
    elif utfCharacter == "x" or utfCharacter == "X":
        keyboard.write(":regional_indicator_x: ")
    elif utfCharacter == "y" or utfCharacter == "Y":
        keyboard.write(":regional_indicator_y: ")
    elif utfCharacter == "z" or utfCharacter == "Z":
        keyboard.write(":regional_indicator_z: ")
    elif utfCharacter == " ":
        keyboard.write(":blue_square: ")
    elif utfCharacter == "1":
        keyboard.write(":one: ")
    elif utfCharacter == "2":
        keyboard.write(":two: ")
    elif utfCharacter == "3":
        keyboard.write("three: ")
    elif utfCharacter == "4":
        keyboard.write(":four: ")
    elif utfCharacter == "5":
        keyboard.write(":five: ")
    elif utfCharacter == "6":
        keyboard.write(":six: ")
    elif utfCharacter == "7":
        keyboard.write(":seven: ")
    elif utfCharacter == "8":
        keyboard.write(":eight: ")
    elif utfCharacter == "9":
        keyboard.write(":nine: ")
    elif utfCharacter == "0":
        keyboard.write(":zero: ")
    elif utfCharacter == "!":
        keyboard.write(":exclamation_mark: ")
    elif utfCharacter == "?":
        keyboard.write(":question: ")
main()