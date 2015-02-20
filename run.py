__author__ = 'matthewgmonteleone'
import mongoengine
from eve import Eve
from eve_mongoengine import EveMongoengine


class Airport(mongoengine.Document):
    id = mongoengine.IntField()
    ident = mongoengine.StringField()
    type = mongoengine.StringField()
    name = mongoengine.StringField()
    lattitude_deg = mongoengine.FloatField()
    longitude_deg = mongoengine.FloatField()
    iso_country = mongoengine.StringField()
    continent = mongoengine.StringField()
    municipality = mongoengine.StringField()
    scheduled_service = mongoengine.StringField()
    iata_code = mongoengine.StringField()
    wikipedia_link = mongoengine.URLField()
    keywords = mongoengine.StringField()
    elevation_ft = mongoengine.IntField()
    meta = {'collection': 'full'}
my_settings = {
    'MONGO_HOST': 'dkr4.aut-aut.rocks',
    'MONGO_PORT': 27018,
    'MONGO_DBNAME': 'airports',
    'DOMAIN': {'airports': {}}, # sadly this is needed for eve
    'XML': False
    ,'QUERY_MAX_RESULTS' : 1000
}


# init application
app = Eve(settings=my_settings)
# init extension
ext = EveMongoengine(app)
# register model to eve
ext.add_model(Airport,
              resource_methods=['GET'],
              additional_lookup = {'field': 'iata_code',
                                   'url': 'regex("[\w]+")'},
              pagination= False
              )
# let's roll
app.run()