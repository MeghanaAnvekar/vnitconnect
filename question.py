class Question(object):
    def __init__(self, qid,question, category, timestamp, tags,user):
        self.qid = qid
        self.question = question
        self.timestamp = timestamp
        self.tags = tags
        self.user = user
        self.category = category

    @staticmethod
    def from_dict(source):

        q = Question(source[u'qid'],source[u'question'],source[u'category'],source[u'timestamp'],source[u'tags'],source[u'user'])
       
	
        if u'question' in source:
            q.question = source[u'question']
        else:
        	print('question not set')
        if u'qid' in source:
            q.qid = source[u'qid']
        else:
        	print('qid not set')
        
        if u'category' in source:
            q.category = source[u'category']
        else:
        	print('cate not set')
        if u'timestamp' in source:
            q.timestamp = source[u'timestamp']
        if u'tags' in source:
            q.tags = source[u'tags']
        if u'user' in source:
            q.user = source[u'user']
	
        return q


    def to_dict(self):
        d = {
            u'question': self.question,
            u'qid': self.qid,
            u'category' : self.category,
            u'timestamp' : self.timestamp,
            u'tags' : self.tags,
            u'user' : self.user

        }

        if self.question:
            d[u'question'] = self.question
        if self.qid:
            d[u'qid'] = self.qid
        if self.category:
            d[u'category'] = self.category
        if self.timestamp :
            d[u'timestamp'] = self.timestamp
        if self.tags :
            d[u'tags'] = self.tags
        if self.user:
            d[u'user'] = self.user

        return d


