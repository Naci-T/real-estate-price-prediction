# Import libraries
from flask import Flask, render_template, redirect, url_for, request, Markup
import pickle
import pandas as pd
app = Flask(__name__)

# Import the model
model = pickle.load(open('model/rf_model.pkl', 'rb'))

# Route to homepage
@app.route('/', methods=['GET'])  
@app.route("/home")
def home():
   return render_template("home.html")

# Route to predict house price
@app.route("/prediction")
def prediction():
    selector = ""
    for i in state_map.keys():
       selector += f"<option value={i}>{i}</option>"
    selector2 = ""
    for i in property_map.keys():
       selector2 += f"<option value={i}>{i}</option>" 
    return render_template("prediction.html", selector = Markup(selector), selector2=Markup(selector2))

# Route to go back to the homepage    
@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# Route that returns the result (prediction) after pressing the submit button
@app.route("/submit", methods=['POST'])   
def submit():    
    # Retrieve the values from form
    postcode=int(request.form['postal'])
    subtype=int(property_map[request.form['sub']])
    number=int(request.form['nr'])
    living_area=int(request.form['larea'])
    terrace_area=int(request.form['tarea'])
    garden_area=int(request.form['garea'])
    surface_area=int(request.form['sarea'])
    state=int(state_map[request.form['stop']])

    # Make a dictionary of the data to give as an input to the model
    dat = {
    'Postal_code': postcode, 
    'Subtype_of_property': subtype, 
    'Number_of_rooms': number, 
    'Living_Area': living_area, 
    'Terrace_Area': terrace_area,
    'Garden_Area': garden_area,
    'Surface_area_of_the_plot_of_land': surface_area, 
    'State_of_the_building': state
        }

    # Make a dataframe with the dictionary and use it to predict the model     
    df = pd.DataFrame(dat, index=[0])
    value = model.predict(df)
    value=int(value)

    return {"prediction": value, "status_code": 200}


# Lists used for dropdown menu in prediction.html: 
state_map = {"AS_NEW": 1, "JUST_RENOVATED": 2, "TO_RESTORE": 3, "GOOD": 4, "TO_RENOVATE": 5, "TO_BE_DONE_UP": 6}
property_map={"PENTHOUSE": 1,"APARTMENT": 2, "DUPLEX": 3, "GROUND_FLOOR": 4, "FLAT_STUDIO": 5,"LOFT": 6, "TRIPLEX": 7, "SERVICE_FLAT": 8, "APARTMENT_GROUP": 9, "KOT": 10, "HOUSE": 11, "HOUSE_GROUP": 12, "APARTMENT_BLOCK": 13, "VILLA": 14, "MANSION": 15, "MIXED_USE_BUILDING": 16, "EXCEPTIONAL_PROPERTY": 17, "COUNTRY_COTTAGE": 18, "BUNGALOW": 19, "TOWN_HOUSE": 20, "FARMHOUSE": 21, "CHALET": 22, "CASTLE": 23, "OTHER_PROPERTY": 24, "MANOR_HOUSE": 25}

if __name__ == '__main__':
   app.run(host='0.0.0.0')