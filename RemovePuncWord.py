# txt = "Imran"
# print(txt.replace(txt[-1], ""))
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            print
            word = word.replace(char,"")
    return word
print(strip_punctuation("#Imran!"))


