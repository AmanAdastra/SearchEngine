from engine.models import Car
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class CarDocument(Document):
    class Index:
        name = 'cars'
        settings = {
            'number_of_shards': 1,
        }

    class Django:
        model = Car
        fields = [
            'id',
            'object_id',
            'maker',
            'model',
            'year',
            'category',
        ]