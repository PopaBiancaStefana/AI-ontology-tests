import random as rand

import lightrdf
from nltk.corpus import wordnet as wn
import re

# nltk.download()
triplets = []


def parse_rdf():
    doc = lightrdf.RDFDocument("ontology/food.rdf")

    # for triple in doc.search_triples(None, None, None):
    #     print(triple)

    return doc


def display_triplets_names():
    global triplets

    doc = parse_rdf()

    for triple in doc.search_triples(None, None, None):
        # check if each element has a name ( has a # in it)
        if "#" in triple[0] and "#" in triple[1] and "#" in triple[2]:
            # get name of each element
            triple = (triple[0].split("#")[-1][:-1], triple[1].split("#")[-1][:-1], triple[2].split("#")[-1][:-1])
            # spaces between words
            triple = (re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', triple[0]),
                      re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', triple[1]),
                      re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', triple[2]))
            triplets.append(triple)

    for triple in triplets:
        print(triple)


def questionnaire():
    global triplets

    question_nr = 0

    while True:
        question_nr += 1
        triple = triplets[question_nr]
        print("Question " + str(question_nr) + ":")

        # remove one element from triplet
        hidden_element = rand.randrange(2)

        if hidden_element == 0:
            question = "What is a " + triple[1] + " of " + triple[2] + "?"
        elif hidden_element == 1:
            question = " What is the relationship between " + triple[0] + " and " + triple[2] + "?"
        else:
            question = "What is the " + triple[1] + " of " + triple[0] + "?"
        print(question)

        answer = input("Answer: ")
        if answer.lower() == triple[hidden_element].lower():
            print("Correct!")
        else:
            print("Incorrect! The correct answer is: " + triple[hidden_element])

        print("Would you like to continue? (y/n)")
        answer = input("Answer: ")
        if answer == "n":
            break


# e nevoie doar de primul sens al cuvantului: de modificat
def get_synonyms(word):
    synonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms
