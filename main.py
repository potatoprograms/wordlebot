file = open("words_alpha.txt")
words = file.readlines()
print("Initializing...")
def remove_newlines(s):
    return s.replace('\n', '')
words = [remove_newlines(item) for item in words]
words = [word for word in words if len(list(word)) == 5]
grays = []
yellows = []
greens = []
print("Please enter any info you have (grays, yellows, greens) in the following format: grays: [letter], yellows: [letter]y[space], greens: [letter]g[space]. To exit: type 'end'")
while True:
    choice = input("")
    if str.lower(choice) == "end":
        break
    if len(list(choice)) == 1:
        grays.append(str.lower(choice))
        continue
    if list(str.lower(choice))[1] == "y":
        yellows.append(list(str.lower(choice)))
        continue
    greens.append(list(str.lower(choice)))
for green in greens:
    my_list = words
    target_letter = green[0]
    words = [word for word in words if word[int(green[2]) - 1] == target_letter]
for gray in grays:
    my_list = words
    target_letter = gray
    words = [word for word in my_list if target_letter not in word]
for yellow in yellows:
    my_list = words
    target_letter = yellow[0]
    words = [word for word in my_list if target_letter in word]
    words = [word for word in words if word[int(yellow[2]) - 1] != target_letter]
print(words)    
