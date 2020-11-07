
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
def mr(p):
    location = geolocator.geocode(p)
    return location
def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    country = address.get('country', '')
    return  country

def mre(l):
    data=pd.read_csv("table-1.csv",index_col=0)
    d=data.loc[:, 'Country':'2017[2][3]']
    d.set_index('Country')
    if str(l) in d.values:
        m=d.loc[d['Country'] == str(l),'2017[2][3]'].iloc[0]
        return m
    else:
        return 0
    
from flask import Flask, request, render_template  
  
# Flask constructor 
app = Flask(__name__)    
  
# A decorator used to tell the application 
#app.config['PYTHONPATH'] = 'backend'
# which URL is associated function 
@app.route('/', methods =["GET", "POST"]) 
def gfg(): 
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       first_name = request.form.get("fname") 
       # getting input with name = lname in HTML form  
        
       p=mr(first_name)
       l=city_state_country(str(p.latitude)+","+str(p.longitude))
       if mre(l)==0:
           output = "No risk is expected based on the data verified"
       else:
           output = "Natural disaster risk is expected with a prediction of "+str(mre(l))
       return render_template('out.html',output=output)
    return render_template("index.html") 
if __name__ == '__main__':
    app.run(debug=True)