i = 0
with open("words_alpha.txt") as f:
    words = f.readlines()
print("Initializing...")
def remove_newlines(s):
    return s.replace('\n', '')

words = [remove_newlines(item) for item in words]
words = [word for word in words if len(word) == 5]
grays = input("Enter all gray letters with no seperating characters").lower()
yellows = input("Enter all yellow letters followed by the position in which they are yellow with no seperating characters").lower()
greens = input("Enter all green letters followed by the position in which they are green with no seperating characters").lower()

while True:
    if i == 1:
        grays = grays + input("Gray additions: ").lower()
        yellows = yellows + input("Yellow additions: ").lower()
        greens = greens + input("Green additions: ").lower()
    yellow_index = range(0, len(yellows))[::2]
    green_index = range(0, len(greens))[::2]

    cleaned_yellows = {}
    for y in yellow_index:
        cleaned_yellows[yellows[y]] = yellows[y+1]
    
    cleaned_greens = {}
    for y in green_index:
        cleaned_greens[greens[y]] = greens[y+1]
    
    for letter, pos in cleaned_greens:
        words = [word for word in words if word[int(pos) - 1] == letter]
    
    for letter, pos in cleaned_yellows:
        words = [word for word in my_list if letter in word]
        words = [word for word in words if word[int(pos) - 1] != target_letter]
    
    for letter in grays:
        words = [word for word in my_list if letter not in word]
   
    print(words)    
    i = 1
    if input("Continue (y/n)").lower() != 'y':
        break
