from sqlalchemy import create_engine, engine
import json

class Db:

    def __init__(self):
        f = open('./config.json')
        data = json.load(f)
        f.close() 
        connection_url = engine.URL.create(
            drivername="mysql",
            username=data['username'],
            password=data['password'],
            host="localhost",
            database="mydb",
        )

        self.eng = create_engine(connection_url, encoding='latin1', echo=True)
        self.eng.connect()