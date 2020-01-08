import click
import random

from faker import Faker

from app.app import create_app
from app.extensions import db
from app.models import User 
from werkzeug.security import generate_password_hash

#create an app context for the database connection.
app = create_app()
db.app = app 

fake = Faker() 


def _log_status(count, model_label):
    """
    Log the output of how many records were created.
    :param count: Amount created
    :type count: int
    :param model_label: Name of the model 
    :type model_label: str
    :return: None
    """
    click.echo('Created {0} {1}'.format(count , model_label))

    return None

def _bulk_insert(model, data, label):
    """
    Bulk insert data to a specific model and log it. This is much more 
    efficient than adding 1 row at a time in a loop.

    :param model: Model being affected
    :type model: SQLAlchemy
    :param data: list
    :param label: Label for the output
    :type label: str
    :return: None
    """
    with app.app_context():
        model.query.delete()
        db.session.commit()
        #bypasses the init function and directly write native sql  to create rows in table
        db.engine.execute(model.__table__.insert(),data)
       

        _log_status(model.query.count(), label)

    return None

@click.group()
def cli():
    """ Add items to database. """
    pass

@click.command()
def users():
    """
    Generate  fake users
    """
    random_emails = []
    data = []

    click.echo("Working.....")

    #Ensure we get about 100 unique emails
    for i in range(0,99):
        random_emails.append(fake.email())
    
    random_emails.append(app.config["SEED_ADMIN_EMAIL"])
    random_emails = list(set(random_emails))

    while True:
        if len(random_emails) == 0:
            break

        #determine if admin or not 

        random_percent = random.random()

        if random_percent >= 0.05:
            is_admin = True
        else:
            is_admin = False
        
        email = random_emails.pop()


        #determine username

        random_percent = random.random()
        
        random_trail = str(int(round(random.random() * 1000)))
        username = fake.first_name() + random_trail
        
    

        #make user object 
        # *multiparams/**params –
        # represent bound parameter values to be used in the execution. Typically, the format is either a collection of one or more dictionaries passed to *multiparams:

        param = {
              "email" : email ,
              "username" : username, 
              "password_hash" : generate_password_hash("password") , 
              "is_admin" : is_admin
        }

        

        #Ensure the seeeded admin always an admin with seeded password 
        if email == app.config["SEED_ADMIN_EMAIL"]:
            password_hash = generate_password_hash(app.config["SEED_ADMIN_PASSWORD"])
            #update dictionary
            param["is_admin"] = True
            param["password_hash"] = password_hash

        data.append(param)
        print(data)

    return _bulk_insert(User, data, 'users')


@click.command()
@click.pass_context
def all(ctx):
    """
    Generate all data.

    :param ctx:
    :return: None
    """
    ctx.invoke(users)

    return None


cli.add_command(all)
cli.add_command(users)
        

        

