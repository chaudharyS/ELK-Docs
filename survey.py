# documents.py

from django_elasticsearch_dsl import DocType, Index,fields
from survey.models import Survey, Category, Question, Response
from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()

survey = Index('surveys') 

@survey.doc_type
class SurveyDocument(DocType):  
    categories = fields.NestedField(properties={
         'name' : fields.TextField(),
         'order' : fields.IntegerField(),
         'description' : fields.TextField(),
    })
    questions = fields.NestedField(properties={
         'text' : fields.TextField(),
         'order' : fields.IntegerField(),
         'required' : fields.BooleanField(),
         'type' : fields.TextField(),
         'choices' : fields.TextField(),
    })
    responses = fields.NestedField(properties={
        'interview_uuid' : fields.TextField(),
    })
    
    class Meta:
        model = Survey
        fields = ['name','description','is_published','need_logged_user']
        related_models = [Category, Question, Response]

    def get_instances_from_related(self, related_instance):
        return self
