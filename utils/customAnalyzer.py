import re

def columnAnalyzer(text):
    features = []
    words = re.findall('([a-z][a-z1-9]*|[1-9]+|[A-Z](?:[a-z1-9]+|[A-Z1-9]+))', text)
    for word in words:
        features.append(word.lower())
    return list(features)