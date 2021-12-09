from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from flask import request, Flask
from flask import request,Flask,render_template,redirect
import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@cluster0.pykpw.mongodb.net/mydb?retryWrites=true&w=majority"
mongo = PyMongo(app)


if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/')
def home():
    # get the notes from the database
    notes = list(mongo.db.notes.find({}).sort("createdAt",-1));

    # render a view
    return render_template("pages/home.html",homeIsActive=True,addNoteIsActive=False,notes=notes)

@app.route("/add-estadistica", methods=['GET','POST'])
def addNote():
    if(request.method == "GET"):

        return render_template("pages/add-estadistica.html",homeIsActive=False,addNoteIsActive=True)

    elif (request.method == "POST"):

        # get the fields data
        name = request.form['name']
        value = request.form['value']
        total = request.form['total']

        # save the record to the database
        mongo.db.notes.insert_one({"name":name,"value":value,"total":total})

        # redirect to home page
        return redirect("/")

@app.route('/tiempo-alistamiento', methods=['GET','POST'])
def editNoteTiempo():

    if request.method == "GET":
        
        # get the note details from the db
        note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b168746eee466439866f81")}))

        # direct to edit note page
        return render_template('pages/edit-tiempo.html',note=note)

    elif request.method == "POST":

        #get the data of the note
        newValue = request.form['value']
        
        # get the note details from the db
        note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b168746eee466439866f81")}))
        total = int(note['total']) + 1
        value = ((int(note['total']) * int(note['value'])) + int(newValue)) / total
        
        # update the data in the db
        mongo.db.notes.update_one({"_id":ObjectId("61b168746eee466439866f81")},{"$set":{"value":value, "total": total }})

        # redirect to home page
        return redirect("/")
    
@app.route('/tiempo-alistamiento/<val>', methods=['GET','POST'])
def editNoteTiempoParam(val):

    #get the data of the note
    newValue = val
    
    # get the note details from the db
    note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b168746eee466439866f81")}))

    total = int(note['total']) + 1
    value = ((int(note['total']) * int(note['value'])) + int(newValue)) / total
    
    # update the data in the db
    mongo.db.notes.update_one({"_id":ObjectId("61b168746eee466439866f81")},{"$set":{"value":value, "total": total }})

    # redirect to home page
    return redirect("/")
    
    
@app.route('/precio', methods=['GET','POST'])
def editNotePrecio():

    if request.method == "GET":
        
        # get the note details from the db
        note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b169780ca1b60f1c3b4dc7")}))

        # direct to edit note page
        return render_template('pages/edit-precio.html',note=note)

    elif request.method == "POST":

        #get the data of the note
        newValue = request.form['value']
        
        # get the note details from the db
        note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b169780ca1b60f1c3b4dc7")}))

        total = int(note['total']) + 1
        value = ((int(note['total']) * int(note['value'])) + int(newValue)) / total
        
        # update the data in the db
        mongo.db.notes.update_one({"_id":ObjectId("61b169780ca1b60f1c3b4dc7")},{"$set":{"value":value, "total": total }})

        # redirect to home page
        return redirect("/")
    
@app.route('/precio/<val>', methods=['GET','POST'])
def editNotePrecioParam(val):

    #get the data of the note
    newValue = val
    
    # get the note details from the db
    note = dict(mongo.db.notes.find_one({"_id":ObjectId("61b169780ca1b60f1c3b4dc7")}))

    total = int(note['total']) + 1
    value = ((int(note['total']) * int(note['value'])) + int(newValue)) / total
    
    # update the data in the db
    mongo.db.notes.update_one({"_id":ObjectId("61b169780ca1b60f1c3b4dc7")},{"$set":{"value":value, "total": total }})

    # redirect to home page
    return redirect("/")

@app.route('/delete', methods=['POST'])
def deleteNote():

    # get the id of the note to delete
    noteId = request.form['_id']

    # delete from the database
    mongo.db.notes.delete_one({ "_id": ObjectId(noteId)})

    # redirect to home page
    return redirect("/")