from django_elasticsearch_dsl import DocType, Index, fields
from survey.models import   Question, Response, Answer
from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()

answer = Index("answers")

@answer.doc_type
class AnswerDocument(DocType):
    question = fields.ObjectField(properties={
         'text' : fields.TextField(),
         'order' : fields.IntegerField(),
         'required' : fields.BooleanField(),
         'type' : fields.TextField(),
         'choices' : fields.TextField(),
    })
    response = fields.ObjectField(properties={
        'interview_uuid' : fields.TextField(),
    })

    class Meta:
        model = Answer
        fields = ['body']
        related_models = [Response, Question]

    
