from django_elasticsearch_dsl import DocType, Index, fields
from survey.models import Survey, Category, Question, Answer
from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()

question = Index('questions')

@question.doc_type
class QuestionDocument(DocType):
    survey = fields.ObjectField(properties={
        'name' : fields.TextField(),
        'description' : fields.TextField(),
        'is_published' : fields.BooleanField(),
        'need_logged_user' : fields.BooleanField(),
    })
    category = fields.ObjectField(properties={
        'name' : fields.TextField(),
        'order' : fields.IntegerField(),
        'description' : fields.TextField(),
    })
    answers = fields.NestedField(properties={
        'body' : fields.TextField(),
    })

    class Meta:
        model = Question
        fields = ['text' , 'order' , 'required' , 'type', 'choices']
        related_models=[Survey, Category, Answer]

    
