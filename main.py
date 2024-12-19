from fastapi import FastAPI
from models import Iphones
from shemas import IphoneSchema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import signal


engine = create_engine('sqlite:///Iphone.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

app = FastAPI()

@app.post('/newiphone')
def add_iphone(iphone:IphoneSchema):
    new_iphone = Iphones(name=iphone.name, battery=iphone.baterry, owner=iphone.owner)
    session.add(new_iphone)
    session.commit()
    return{"message":"Новый айфон добавлен", "его айди": new_iphone.id}

@app.get('/iphones')
def get_iphones():
    iphones = session.query(Iphones).all()
    result = [
        {"name":iphone.name, "battery":iphone.battery, "owner":iphone.owner}
        for iphone in iphones
    ]
    return result


    @app.get("/shutdown")
    def shutdown():
        os.kill(os.getpid(), signal.SIGINT)
        return {"message": "Shutting down..."}

