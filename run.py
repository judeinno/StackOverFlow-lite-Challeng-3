from app import create_app
from instance.config import DevelopmentConfig
from app.models.User_DBmanager import DBManager

# The initialisation allows me to create the app in my run file where i will be running my app
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    manager = DBManager()
    manager.create_tables()
    app.run()
