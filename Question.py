class Question(object):
    def __init__(self, qid,question, category, timestamp, tags,user):
        self.qid = qid
        self.question = question
        self.timestamp = timestamp
        self.tags = tags
        self.user = user

    @staticmethod
    def from_dict(source):

        q = Question(source[u'question'])

        if u'question' in source:
            q.question = source[u'question']

        return q


    def to_dict(self):
        d = {
            u'question': self.question
        }

        if self.question:
            dest[u'question'] = self.question

        return d

    def __repr__(self):
        return u'City(question={})'.format(
            self.qid, self.question, self.timestamp, self.tags,self.user)
