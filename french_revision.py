import codecs
from random import randint

###LIST HANDLING FUNCTIONS
def handle_duplicates(l):
    new = []
    for word in l:
        found = False
        for i in range(0, len(new)):
            if word[1:len(word)-1] == new[i][1:len(new[i])-1]:
                found = True
                index = i
        if not found:
            new.append(word)
        else:
            new[index][len(new[index])-1] += ", " + word[len(word)-1].strip()
    return new

def list_to_string(l):
    string = ""
    for s in l:
        string += s.strip() + " "
    return string

###OPTIONS FUNCTIONS
def option_list():
    for i in range(0, 1000):
        user_input = input("Word {}: {} ->".format(list_of_words[i][0], list_to_string(list_of_words[i][1:len(list_of_words[i])-1])))
        if user_input == "exit":
            break
        print(list_of_words[i][len(list_of_words[i])-1].strip())

def option_random():
    random_list = list(list_of_words)
    while len(random_list) > 0:
        random_int = randint(0, len(random_list)-1)
        word = random_list.pop(random_int)
        user_input = input("Word {}: {} ->".format(word[0], list_to_string(word[1:len(word)-1])))
        if user_input == "exit":
            break
        print(word[len(word)-1].strip())

def option_between():
    start = int(input("Start: "))
    end = int(input("End: "))
    for i in range(start, end):
        if i > len(list_of_words)-1:
            break
        user_input = input("Word {}: {} ->".format(list_of_words[i][0], list_to_string(list_of_words[i][1:len(list_of_words[i])-1])))
        if user_input == "exit":
            break
        print(list_of_words[i][len(list_of_words[i])-1].strip())

def option_display():
    start = int(input("Start: "))
    end = int(input("End: "))
    for i in range(start, end):
        if i > len(list_of_words)-1:
            break
        print("Word {}: {} -> {}".format(list_of_words[i][0], list_to_string(list_of_words[i][1:len(list_of_words[i])-1]), list_of_words[i][len(list_of_words[i])-1].strip()))

###MAIN FUNCTION
def main():
    while True:
        user_input = ""
        while user_input not in VALID_INPUTS:
            user_input = input("[l]ist\n[r]andom\n[b]etween\n[d]isplay\n")
        if user_input == "l":
            option_list()
        elif user_input == "r":
            option_random()
        elif user_input == "b":
            option_between()
        elif user_input == "d":
            option_display()

###RUN APP

VALID_INPUTS = ["l", "r", "b", "d"]

list_of_words = []
file = codecs.open(r'french_1000_words.txt', encoding='utf-8')
lines = file.readlines()
count = 0
for line in lines:
    count += 1
    line_list = line.strip().split(' ')
    list_of_words.append(line_list)
list_of_words = handle_duplicates(list_of_words)

main()
