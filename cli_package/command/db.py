import click 

from sqlalchemy_utils import database_exists, create_database 

from app.app import create_app
from app.extensions import db
from app.models import User

#create an app context for the database connection.
app = create_app()
db.app = app 


@click.group()
def cli():
    """ Run PostgreSQL related tasks. """

@click.command()
@click.option('--with-testdb/--no-with-testdb' , default=False,
                help="create a test db too?")
def init(with_testdb):
    """
    Initialize the database.

    :param with_testdb: Create a test database 
    :return: None
    """
    db.drop_all()
    db.create_all()

    if with_testdb:
        db_uri = '{0}_test'.format(app.config['SQLALCHEMY_DATABASE_URI'])

        if not database_exists(db_uri):
            create_database(db_uri)
    
    return None

@click.command()
def seed():
    """
    Seed the database with initial user.

    :return: User instance
    """
    if User.find_by_identity(app.config['SEED_ADMIN_EMAIL']) is not None:
        return None
    
    u = User(email=app.config['SEED_ADMIN_EMAIL'] , username='admin' , password = app.config['SEED_ADMIN_PASSWORD'] , is_admin=True)
    db.session.add(u)
    db.session.commit()

@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False,
                        help='Create a test db too?')
@click.pass_context
def reset(ctx,with_testdb):
    """
    Init and seed automatically.

    :param with_testdb: Create a test database
    :return: None 
    """
    ctx.invoke(init, with_testdb=with_testdb)
    ctx.invoke(seed)

    return None


cli.add_command(init)
cli.add_command(seed)
cli.add_command(reset)


