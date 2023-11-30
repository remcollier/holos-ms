from flask import Flask,request,Response,redirect
from os import environ
# from sqlalchemy import create_engine, MetaData, \
#     Column, Integer, Numeric, String, Date, Table, ForeignKey

# Constants
HOST=environ.get('HOST', 'localhost')
PORT=environ.get('PORT', 8088)

BASE_URL='http://'+HOST+':'+str(PORT)+'/'

FAKE_DATABASE = {}

# # Set up connection between sqlalchemy and postgres dbapi
# engine = create_engine(
#     "postgresql://postgres:postgres@localhost:5432/fakedata"
# )# Create a metadata object
# metadata = MetaData()

# Main Code
app = Flask(__name__)

@app.route('/farms',methods=['GET','POST'])
def farms():
    if request.method == "GET":
        farms = []
        for id, farm in FAKE_DATABASE.items():
            farm['@id']=BASE_URL+'farms/'+id
            farms.append(farm)
        return farms
    else:
        data =request.json

        size = len(FAKE_DATABASE.keys())
        
        # Store Data
        FAKE_DATABASE[str(size)]=data

        # Create URL
        url = BASE_URL+'farms/'+str(size)

        # Return response...
        return Response("", status=201, headers={'Location':url})
    
@app.route('/farms/<id>',methods=['GET','POST'])
def farm(id):
    farm = FAKE_DATABASE[id]
    farm['@id']=BASE_URL+'farms/'+id
    return farm


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=PORT)
