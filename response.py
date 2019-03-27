from django_elasticsearch_dsl import DocType, Index, fields
from survey.models import Survey, Response, Answer
from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()

response = Index("responses")

@response.doc_type
class ResponseDocument(DocType):
    survey = fields.ObjectField(properties={
        'name' : fields.TextField(),
        'description' : fields.TextField(),
        'is_published' : fields.BooleanField(),
        'need_logged_user' : fields.BooleanField(),
     })
    answers = fields.NestedField(properties={
        'body' : fields.TextField(),
            })

    class Meta:
        model = Response
        fields = ['interview_uuid']
        related_models = [Survey, Answer]

    
