# Imports
#NLTK_DATAimport nltk

# Imports
import nltk
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
import os

#categories
categories = {
'hostel':['hostel','girls hostel','boys hostel'],
'events':['aarohi','axis','consortium','conso','ig','js','junior scientist','institute gathering','dg','department gathering','dept gathering','cultural events'],
'contact':['email','mobile','mobile no','phone','address'],
'placements':['day one companies','recruiters','amazon','morgan stanley','goldman sacchs','internships','intern','package','placed','placements'],
'registration':['course registration'],
'library':['library'],
'career':['mtech','gre','GATE','gate exam','cat exam','CAT','iim','iit','career'],
'projects':['project','research','projects'],
'clubs':['ecell','e-cell','octaves','grooves','prayaas','mag.com','astronomy','ivlabs','tesla','club capture','iridiscence','halla bol','clubs'],
'academics':['study','toc','lp','dspd','compilers','os','operating systems','sessional','end sem','time table','credits'],
}

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

def lemmatize(a):
    print("entering lemmatize")
    # Get default English stopwords and extend with punctuation
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(string.punctuation)
    stopwords.append('')
    # Create tokenizer and stemmer
    tokenizer = nltk.tokenize
    lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

    a_tagged = nltk.word_tokenize(a)
    pos_a = map(get_wordnet_pos, nltk.pos_tag(a_tagged))
    print(pos_a)
    lemmae_a = []
    for token, pos in pos_a:
        temp = token.lower().strip(string.punctuation)
        print(temp)
        if temp not in stopwords:
            print("true")
            u = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(temp)
            print("u = "+u)
            lemmae_a.append(temp)
    """lemmae_a = [nltk.stem.wordnet.WordNetLemmatizer().lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]"""
    print("printing lemma_e")
    print(lemmae_a)
    print("leaving lemmatize")
    return lemmae_a

def is_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    print("entering is_match")
    lemmae_a = lemmatize(a)
    lemmae_b = lemmatize(b)
    # Calculate Jaccard similarity
    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    print("leaving is_match")
    return (ratio)


if __name__ == '__main__':
    print(is_match('where is vnit',"what is vnit's location"))
    print(is_match('how to score better marks','how to study well'))
    print(is_match('when is first sessional?',"when is first sessional"))
