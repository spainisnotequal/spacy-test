import spacy
nlp = spacy.load("es_core_news_sm")


def tag(sentence):
    tags = nlp(sentence)
    result = []
    for token in tags:
        result.append([token.text, token.lemma_, token.pos_, token.tag_,
                       token.dep_, token.shape_, token.is_alpha, token.is_stop])
    return result


if __name__ == "__main__":
    import sys
    print(tag(sys.argv[1]))
