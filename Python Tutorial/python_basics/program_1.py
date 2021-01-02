def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "%s?" % capitalized
    else:
        return "%s." % capitalized

print(sentence_maker("how are you"))


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

# join() method takes all items in an iterable and joins them into one string
# string.join(iterable) with the string inserted between each item in iterable   
print(" ".join(results))
