"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
my_brand = Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
my_model = Model.query.filter_by(name = 'Corvette', brand_name = 'Chevrolet').all()

# Get all models that are older than 1960.
my_models = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
my_brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
my_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
my_brands = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
my_brands = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()

# Get any model whose brand_name is not Chevrolet.
my_models = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    my_models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand, Model.brand_name == Brand.name).all()

    for model in my_models:
        name, brand_name, headquarters = model
        print "Name: {}, Brand name: {}, Headquarters: {}".format(name, brand_name, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    my_brands = db.session.query(Brand.name, Model.name).join(Model, Model.brand_name == Brand.name).all()

    brand_names = []

    for item in my_brands:
        brand_name, model_name = item
        if brand_name not in brand_names:
            print "BRAND: {}\nModel name: {}".format(brand_name, model_name)
            brand_names.append(brand_name)
        else:
            print "Model name: {}".format(model_name)
        # print "Brand name: {}, Model name:{}".format(brand_name, model_name)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# This is a query object. Since you haven't yet extracted any values from it (with .all(), .one(), etc.)
# it will just function as an object that queries for all the items in the brand table with the name "Ford".

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#An association table is a table that is set up to build a relationship between two other tables.
#This is set up to structure a "many to many" relationship. Specifically, the association table (as opposed
    # to the "middle table") doesn't have meaningful fields - it just provides a connection between the other two tables.

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):

    brands = Brand.query.filter(Brand.name.like("%"+mystr+"%")).all()

    return brands


def get_models_between(start_year, end_year):

    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

    return models
