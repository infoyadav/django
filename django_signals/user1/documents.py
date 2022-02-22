# To make this model work with Elasticsearch, create a subclass of django_elasticsearch_dsl.Document, 
# create a class Index inside the Document class to define your Elasticsearch indices, names, settings 
# etc and at last register the class using registry.register_document decorator. 
# It required to defined Document class in documents.py in your app directory.


# from django_elasticsearch_dsl import Document
# from django_elasticsearch_dsl.registries import registry
# from .models import Category

# @registry.register_document
# class CategoryDocument(Document):
#     class Index:
#         name = 'category'
    
#     settings = {
#         'number_of_shards': 1,
#         'number_of_replicas': 0
#     }
    
#     class Django:
#         model = Category
#         fields = [
#             'name',
#             'desc',
#         ]
# Populate:
# To create and populate the Elasticsearch index and mapping use the search_index command: $python manage.py search_index — rebuild
# For more help use $python manage.py search_index — help command
# Now, when you do something like:


from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Car


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'cars'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Car # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'color',
            'description',
            'type',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000