from flask import Flask, render_template, redirect, url_for, request, Markup
import pickle
import pandas as pd
app = Flask(__name__)

#import the model
model = pickle.load(open('model/rf_model.pickle', 'rb'))

@app.route('/', methods=['GET'])  
@app.route("/home")
def home():
   return render_template("home.html")

#province_list=['Brussels','Walloon Brabant','West Flanders','East Flanders','Liège', 'Hainaut', 'Luxembourg','Flemish Brabant','Namur','Antwerp','Limburg']

@app.route("/prediction")
def prediction():
    #selector = ""
    #for i in province_list:
    #    selector += f"<option value={i}>{i}</option>"
    #return render_template("prediction.html", selector = Markup(selector))
    return render_template("prediction.html")
    
@app.route("/logout")
def logout():
    return redirect(url_for("home"))

@app.route("/submit", methods=['POST'])   
def submit():
    #province=request.form['provinces']
    postcode=int(request.form['postal'])
    subtype=int(request.form['sub'])
    number=int(request.form['nr'])
    living_area=int(request.form['larea'])
    terrace_area=int(request.form['tarea'])
    garden_area=int(request.form['garea'])
    surface_area=int(request.form['sarea'])
    state=int(request.form['stop'])

    #make a dict of the data
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

    #predict using model     
    df = pd.DataFrame(dat, index=[0])
    value = model.predict(df)
    value=int(value)

    return {"prediction": value, "status_code": 200}


if __name__ == '__main__':
   app.run(host='0.0.0.0')

