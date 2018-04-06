#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
#from firestore import DocumentReference
from nlp import categories, lemmatize
from question import Question
# Use a service account
#cred = credentials.Certificate('vnit-connect-firebase-adminsdk-2g8bd-ac564092f3.json')
#firebase_admin.initialize_app(cred)

#db = firestore.client()
from google.cloud import firestore
import google.cloud.exceptions

db = firestore.Client()


def fetch_data(q):
    lemmae_q = lemmatize(q)
    category = 'misc'
    for x in lemmae_q:
        for y in categories:
            for z in y:
                if x == z:
                    category = y
                    break

    docs = db.collection(u'questions').get()
    #where(u'category', u'==',category).get()
    #questions = Question.from_dict(docs.to_dict())
    #questions =next(questions,None)
    print( Question.from_dict(docs.to_dict()))

    return


if __name__ == '__main__':
    fetch_data('When is the first sessional?')
    fetch_data('Where is VNIT?')
