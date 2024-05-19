from textblob import TextBlob
from gingerit.gingerit import GingerIt

def correct_spell(self,text):
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = str(TextBlob(word).correct())
        corrected_words.append(corrected_word)
    return " ".join(corrected_words)
def correct_grammar(self,text):
    matches = self.grammar_check.parse(text)
    foundmistakes = []
    for error in matches['corrections']:
        foundmistakes.append(error['text'])
    foundmistakes_count = len(foundmistakes)
    return foundmistakes,foundmistakes_count

message = "Hello world. I like mashine learning. appple. bananana"
print(correct_spell(message))
print(correct_grammar(message))