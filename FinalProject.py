# Removes punctuation from word
def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            print
            word = word.replace(char, "")
    return word

# It returns the total negative word count
def get_neg(str):
    str = strip_punctuation(str).lower()
    count = 0
    for word in str.split():
        if word in negative_words:
            count = count + 1
    return count

# It returns the total positive word count
def get_pos(str):
    str = strip_punctuation(str).lower()
    count = 0
    for word in str.split():
        if word in positive_words:
            count = count + 1
    return count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use

# Its give positive words only and save in positive_word list
positive_words = []
with open("positive_words.txt") as pos_f:
   for lin in pos_f:
       if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())

# Its give negative words only and save in negative_word list
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


count = 0
noOfRetweet = []
noOfReplies = []
pcount = []
ncount = []

fileobj = open("project_twitter_data.csv", "r")
content = fileobj.readlines()

for line in content[1:]:
    value = line.split(",")
    noOfRetweet.append(value[1])
    noOfReplies.append(value[2].strip())
    pcount.append(get_pos(value[0]))
    ncount.append(get_neg(value[0]))
    count += 1

netScore = [p-n for p, n in zip(pcount,ncount)] # zip get 1st element from pcount and ncount, perform action(p-n) save in a list.Similarly perform with the rest of the element.

fileobj2 = open("resulting_data.csv", "w")
fileobj2.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fileobj2.write('\n')
i = 0

while i < count:
    row_string = '{},{},{},{},{}'.format(noOfRetweet[i], noOfReplies[i], pcount[i], ncount[i], netScore[i])
    print(row_string)
    fileobj2.write(row_string)
    fileobj2.write('\n')
    i += 1
fileobj2.close()
