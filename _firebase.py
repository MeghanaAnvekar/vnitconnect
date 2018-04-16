import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from nlp import categories, is_match, lemmatize
from question import Question
import os
import sys

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'vnit-connect-firebase-adminsdk-2g8bd-ac564092f3.json'
cred = credentials.Certificate('vnit-connect-firebase-adminsdk-2g8bd-ac564092f3.json')
firebase_admin.initialize_app(cred)
db = firestore.Client()
print(sys.version)

def fetch_data(q):
	lemmae_q = lemmatize(q)
	print(lemmae_q)
	category = 'misc'
	print(type(category))
	
	for x in categories:
		for y in categories[x]:
			for z in lemmae_q:	
				if z == y:
			    		category = x
			    		print("match =>"+category)
			    		break
	u1 = category#.decode('utf-8')
	
	docs = db.collection('questions').get()#where('category', '==',u1).get()
	
	qid = 0
	threshold = 0
	for doc in docs:
		w = Question.from_dict(doc.to_dict())
		match_percent = is_match(w.question,q)
		if match_percent > threshold :
			qid = w.qid
			threshold = match_percent
			print(str(qid)+" "+w.question)
	final_ans = "Sorry I don't know the answer"
	upvotes = 0
	if qid != 0 and threshold >= 0.5 :
		ans_docs = db.collection(u'answers').get()#where(u'qid', u'==',qid).get() 
	
		for doc in ans_docs:
			ans = doc.to_dict()
			if upvotes < ans[u'upvotes']:
				upvotes = ans[u'upvotes']
				final_ans = ans[u'answer']
				
		


	return (final_ans)


def fetch_questions(q):
	lemmae_q = lemmatize(q)
	print(lemmae_q)
	category = 'misc'
	
	for x in categories:
		for y in categories[x]:
			for z in lemmae_q:	
				if z == y:
			    		category = x
			    		print("match =>"+category)
			    		break
	u1 = category#.decode('utf-8')
	print(type(u1))
	
	docs = db.collection(u'questions').where(u'category', u'==',u1).get()
	
	qid = []
	threshold = 0.4
	for doc in docs:
		w = Question.from_dict(doc.to_dict())
		match_percent = is_match(w.question,q)
		if match_percent >= threshold :
			qid.append(w.qid)
			
	print(qid)
	return qid


if __name__ == '__main__':
    #fetch_data('When is the first sessional?')
    fetch_questions('Where is VNIT?')
    fetch_questions('When is the first sessional?')
    
