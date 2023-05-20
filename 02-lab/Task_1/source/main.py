import functions

text = '''Thank you -- all of these performances were impeccable. In my opinion I didn't see a false note anywhere. I want to thank Jean-Marc Vallee our director. I want to thank Jared Leto and Jennifer Garner who I worked with daily.

There are three things that I need each day. One, I need something to look up to, another to look forward to, and another is someone to chase.

First off, I want to thank God because that's who I look up. He's graced my life with opportunities that I know are not of my hand or of any other hand. He's shown me that it's a scientific fact that gratitude reciprocates.

To my family is to what I look forward to. To my father who I know is up there right now with a big pot of gumbo, he has a big lemon meringue pie over there. He's probably in his underwear and has a big can of Miller Lite and he's dancing right now. To you dad, you taught me how to be a man.

To my mother who's here tonight, who taught me and my two older brothers -- demanded -- that we respect ourselves. And in turn we learned we were better able to learn how to respect others. Thank you for that mama.

To my wife, Camilla, and my kids Levi, Vida and Mr Stone (Livingstone), the courage you give me every time I walk through the door is unparallelled. You are the four people in my life that I want to make the most proud of me. Thank you.
And to my hero. That's who I chase. When I was 15 years old I had a very important person in my life come and ask me 'Who's your hero?' I said, 'I thought about it and it's me in ten years. So I turned 25 ten years later and that same person comes to me and goes, 'Are you a hero?' I said, 'Not even close!' She said why and I said, 'My hero is me at 35.' You see, every day, and every week, and every month, and every year of my life, my hero is always ten years away. I'm never going to be my hero. I'm not going to obtain that and that's fine with me because it keeps me with somebody to keep on chasing.

So to any of us, whatever those things are and whatever it is we look up to, whatever it is we look forward to and whoever it is we're chasing, to that I say Amen. To that I say alright, alright, alright. And just keep living, huh? Thank you.'''

# test_text = '''Hello, Mr.Bond, do you think it's sunny today?? Oh, really ..?!! I think so to...'''
test_text = "Abc... Abc?! Abc!!! Mr. Abc: Abc, Abc, Abc."

sentences = functions.count_sentences(test_text)
nondeclarative_sentences = functions.count_nondeclarative_sentences(test_text)
average_sentence_length = functions.avg_sentence_length(test_text)
average_word_length = functions.avg_word_length(test_text)
top_10_ngrams = functions.top_k_ngrams(test_text)

print(functions.avg_sentence_length('''Hello! How are Mr.Ben 123 sldkfj12 you? I'm doing well.'''))
print(9/3)

print(f"Number of sentences in the text: {sentences}")
print(f"The number of non-declarative sentences in the text: {nondeclarative_sentences}")
print(f"Average sentence length in characters: {average_sentence_length:.2}")
print(f"The average length of a word in the text in characters: {average_word_length:.2}")
print("Top 10 repetitive 4-grams in the text:")
for item in top_10_ngrams.items():
    print(item)