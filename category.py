from django_elasticsearch_dsl import DocType, Index, fields
from survey.models import Survey, Category,Question
from elasticsearch_dsl.connections import connections
# Create a connection to ElasticSearch
connections.create_connection()

category = Index("categories")

@category.doc_type
class CategoryDocument(DocType):
    survey = fields.ObjectField(properties={
        'name' : fields.TextField(),
        'description' : fields.TextField(),
        'is_published' : fields.BooleanField(),
        'need_logged_user' : fields.BooleanField(),
    })
    questions = fields.NestedField(properties={
         'text' : fields.TextField(),
         'order' : fields.IntegerField(),
         'required' : fields.BooleanField(),
         'type' : fields.TextField(),
         'choices' : fields.TextField(),
    })

    class Meta:
        model = Category
        fields = ['name', 'order', 'description']
        related_models = [Survey,Question]




