from app import create_app
from instance.config import app_config
from app.models.User_DBmanager import DBManager

# The initialisation allows me to create the app in my run file where i will be running my app
app = create_app('development')

if __name__ == '__main__':
    manager = DBManager(app.config['DATABASE_URL'])
    manager.create_tables()
    app.run()
