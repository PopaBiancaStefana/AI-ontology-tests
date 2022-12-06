import lightrdf
import nltk
from nltk.corpus import wordnet as wn
# nltk.download()

def parse_rdf():
    # parser = lightrdf.Parser()
    #
    # for triple in parser.parse("ontology/food.rdf", base_iri=None):
    #     print(triple)

    doc = lightrdf.RDFDocument("ontology/food.rdf")

    for triple in doc.search_triples(None, None, None):
        print(triple)


# e nevoie de primul sens pt punctele urmatoare
def get_synonyms(word):
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


def main():
    parse_rdf()
    print(get_synonyms("wine"))



if __name__ == '__main__':
    main()
