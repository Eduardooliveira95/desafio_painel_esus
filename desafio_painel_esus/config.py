import os


class Config:
    DEBUG = True
    PORT = 3306
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'urubu100')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'desafio_esus')
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

   

