text="abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper()) # is the text all uppercase?
print("ABC".isupper()) # is the text all uppercase?
print(text.upper()) # convert the text to uppercase
print(text.upper().isupper()) #is the text all uppercase? yes

new_text = text.upper()
print(text, new_text)
print("bannnannnaana".count("n"))
print("banabababnan".index("ana"))
print("banababananabnana".replace("ana", "XXYYZZ"))
sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, " ")
print(sentence)

print("this is a sentence and I want the words".split(" "))

text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob. such a nice guy Bob is"
print(text.find("Bob"))
print(text.rfind("Bob"))
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1