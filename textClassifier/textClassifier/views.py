from django.shortcuts import render
from textblob import TextBlob


def index(request):
    return render(request, 'index.html')


def translate(request):
    input_text = request.POST.get('text', 'default')

    pos = request.POST.get('pos', 'off')
    sentiment = request.POST.get('sentiment', 'off')

    if pos == "on":
        r = ""
        blob_object = TextBlob(input_text)

        for i in blob_object.tags:
            if i[1] == "NNP":
                r += str(i[0]) + ": Proper Noun, Singular object!" + "\n"
            if i[1] == "NN":
                r += str(i[0]) + ": Common Noun, Singular object!" + "\n"
            if i[1] == "NNPS":
                r += str(i[0]) + ": Proper Noun, Plural object!" + "\n"
            if i[1] == "NNS":
                r += str(i[0]) + ": Common Noun, Plural object!" + "\n"
            if i[1] == "VBZ":
                r += str(i[0]) + ": Verb, 3rd person singular object!" + "\n"
            if i[1] == "JJ":
                r += str(i[0]) + ": Adjective!" + "\n"
            if i[1] == "MD":
                r += str(i[0]) + ": Modal!" + "\n"
            if i[1] == "VB":
                r += str(i[0]) + ": Verb!" + "\n"
            if i[1] == "IN":
                r += str(i[0]) + ": Preposition!" + "\n"
            if i[1] == "DT":
                r += str(i[0]) + ": Determiner!" + "\n"
            if i[1] == "CC":
                r += str(i[0]) + ": Coordinating Conjunction!" + "\n"
            if i[1] == "PRP":
                r += str(i[0]) + ": Personal Pronoun!" + "\n"
            if i[1] == "PRP$":
                r += str(i[0]) + ": Possesive Pronoun!" + "\n"
            if i[1] == "RB":
                r += str(i[0]) + ": Adverb!" + "\n"
            if i[1] == "VBG":
                r += str(i[0]) + ": Verb- Gerund!" + "\n"
            if i[1] == "UH":
                r += str(i[0]) + ": Interjection!" + "\n"
            if i[1] == "WP":
                r += str(i[0]) + ": wh-pronoun!" + "\n"
            if i[1] == "WRB":
                r += str(i[0]) + ": wh-adverb!" + "\n"
            if i[1] == "VBP":
                r += str(i[0]) + ": Verb!" + "\n"
            if i[1] == "VBD":
                r += str(i[0]) + ": Verb, past tense!!" + "\n"
            if i[1] == "VBN":
                r += str(i[0]) + ": Verb, past participle!!" + "\n"

        params = {'purpose': 'Classified Text', 'converted_text': r}
        return render(request, 'analyze.html', params)
    elif sentiment == "on":
        classify = TextBlob(input_text)
        value = classify.sentiment.polarity
        if value < 0:
            r = "It's a Negative Sentence"
        elif value == 0:
            r = "It's a Neutral sentence"
        elif value > 0 and value <= 1:
            r = "It's a Positive sentence."
        params = {'purpose': 'Analyzed Text', 'converted_text': r}
        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': 'Analyzed Text', 'converted_text': "No Option is chosen!!"}
        return render(request, 'analyze.html', params)
