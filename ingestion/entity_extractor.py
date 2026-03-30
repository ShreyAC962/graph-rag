# Used for NLP tasks : entity recognition and parsing etc 
import spacy 

# Loads a pretrained English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text : str):
    # Converts raw text into a Doc object (tokens + linguistic features)
    docs = nlp(text)
    entities = []
    for ent in docs.ents:
        # ent.text → actual word, ent.label_ → type
        entities.append((ent.text, ent.label_))
    return entities



# Subject → Verb → Object
def extract_relations(text):
    docs = nlp(text)
    relations = []
    # token is a word or punctuation
    for token in docs:
        # If main verb
        if token.dep_ == "ROOT":
            # nsubj = normal subject, nsubjpass = passive subject
            # dobj = direct object, pobj = object of preposition
            subject = [w for w in token.lefts if w.dep_ in ("nsubj", "nsubjpass")]
            object = [w for w in token.rights if w.dep_ in ("dobj", "pobj")]
            if subject and object:
                relations.append(subject[0].text, token.text, object[0].text)
    return relations

