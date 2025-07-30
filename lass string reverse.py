class ReverseWords:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        words = self.sentence.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)


text = input("Enter a sentence: ")
reverser = ReverseWords(text)
print("Reversed sentence:", reverser.reverse())
