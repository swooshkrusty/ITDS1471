
#Name: Andrei Tsenev
#Date: September 14, 2026
#Module: 03REV – Review Python Fundamentals

'''Description: This program asks the user to enter a text string.
It converts the text to uppercase so vowels are counted consistently.
Each character is checked against a dictionary containing the five vowels.
The program updates individual vowel counts and tracks the total.
A separate function displays the results in a formatted report.
Text without vowels produces a report with all counts equal to zero.'''


# CONSTANTS
TITLE = "Welcome to vowel counter program!"
PROMPT = "Enter any text: "
LINE = "-"
REPORT_LIST = ["VOWEL COUNT REPORT:", "Vowel", "Count", "Total"]
VOWELS = ["A", "E", "I", "O", "U"]
REPORT_WIDTH = 20


'''
The main function displays the welcome message and collects the user's text.
It passes the text to the counting function and sends the returned results
to the report function.
'''
def main():
    print(TITLE)
    print(LINE * len(TITLE))
    text = input(PROMPT).upper()

    vDict, total = findVowelCount(text)
    generateReport(vDict, total)


'''
This function receives a text string and checks each character for a vowel.
It returns both a dictionary of individual counts and the total vowel count.
'''
def findVowelCount(text):
    vDict = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    total = 0

    for character in text:
        if character in vDict:
            vDict[character] += 1
            total += 1

    return vDict, total


'''
This function receives the vowel dictionary and total count.
It prints a table containing each vowel's count and the overall total.
It displays the report without returning a value.
'''
def generateReport(vDict, total):
    print()
    print(REPORT_LIST[0])
    print(LINE * REPORT_WIDTH)
    print(f"{REPORT_LIST[1]:<10}{REPORT_LIST[2]:>10}")
    print(LINE * REPORT_WIDTH)

    for vowel in VOWELS:
        print(f"{vowel:<10}{vDict[vowel]:>10}")

    print(LINE * REPORT_WIDTH)
    print(f"{REPORT_LIST[3]:<10}{total:>10}")
    print(LINE * REPORT_WIDTH)


main()