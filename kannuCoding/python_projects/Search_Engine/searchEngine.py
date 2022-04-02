import time
dataf = open("data.txt")

def match_browse(sentence1, sentence2):
    sentence1_list = sentence1.split(" ")
    sentence2_list = sentence2.split(" ")
    matches = 0

    for word1 in sentence1_list:
        for word2 in sentence2_list:
            if word2 == word1:
                matches += 1

    return matches

data = [d for d in dataf.read().split("->")]

while True:
    query = input("Enter query: ")

    time_init = time.time()
    matches_data = sorted(zip([match_browse(item.lower(), query.lower()) for item in data], data), reverse=True)

    matches = []
    for i in matches_data:
        if i[0] != 0:
            matches.append(i)
            
    print(f"\n{len(matches)} {'result' if len(matches) == 0 or len(matches) == 1 else 'results'} found({time.time() - time_init} s)\n")

    for item in matches:
        print(f"[{matches.index(item) + 1}]. {item[1]}", end="\n\n")

    # asking for exit
    if input("\n\nenter 'q' to exit...") == "q":
        break
