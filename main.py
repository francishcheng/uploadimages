from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import matplotlib.pyplot as plt
IMG_SAVE_PATH = '/var/www/html/img/'
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    points: str
    TABLE: str
    RecordID: str


@app.post("/items/")
async def create_item(item: Item):
    TABLE = item.TABLE
    RecordID = item.RecordID
    points = item.points
    points = [int(point) for point in points.split(',')[:-1]]

    fig, ax = plt.subplots()
    ax.plot(range(len(points)), points)             
    plt.savefig('{IMG_SAVE_PATH}{TABLE}_{RecordID}.png'.format(IMG_SAVE_PATH=IMG_SAVE_PATH, TABLE=TABLE, RecordID=RecordID))
    plt.close()
    print(str(RecordID) + 'saved')
    return {'msg': 'saved!'}
