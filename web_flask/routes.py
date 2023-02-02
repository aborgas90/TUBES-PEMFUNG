from web_flask import app
from flask import render_template
import json
import urllib.request

#calling data json
url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
f = urllib.request.urlopen(url).read().decode()
data = json.loads(f) #serializing data json object
data = data["Infogempa"]["gempa"] #object

datagempa = []
for i in range(len(data)):
    gempa = dict()
    gempa['Tanggal'] = data[i]['Tanggal']
    gempa['Jam'] = data[i]['Jam']
    gempa['DateTime'] = data[i]['DateTime']
    gempa['Coordinates'] = data[i]['Coordinates']
    gempa['Lintang'] = data[i]['Lintang']
    gempa['Bujur'] = data[i]['Bujur']
    gempa['Magnitude'] = data[i]['Magnitude']
    gempa['Kedalaman'] = data[i]['Kedalaman']
    gempa['Wilayah'] = data[i]['Wilayah']
    gempa['Potensi'] =  data[i]['Potensi']
    datagempa.append(gempa)

def filter(datagempa):
    filter_gempa = []
    for i in range(len(datagempa)):
        if float (datagempa[i]['Magnitude']) >= 5.5:
            filter_gempa.append(datagempa[i])
    return filter_gempa
hasilfilter = filter(datagempa)
print(hasilfilter)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    datakelompok =[
        {
            "gambar": "https://cdn.discordapp.com/attachments/1006398819753263126/1066594100930941018/avatar5.png",
            "nim" : "21102034",
            "nama" : "Aditya Stiawan"
        },
        {
            "gambar":"https://cdn.discordapp.com/attachments/1006398819753263126/1066594126348423198/avatar4.png",
            "nim" : "21102022",
            "nama": "Muhhamad Wildan Nugroho"
        },
        {
            "gambar":"https://cdn.discordapp.com/attachments/1006398819753263126/1066594146296541325/avatar2.png",
            "nim" : "2110202",
            "nama": "Bagus Mustaqiem Alfan Zulkarnain"
        }
    ]
    return render_template('about.html',len = len(datakelompok), datakelompok = datakelompok)

@app.route('/home')
def home():
    return render_template('home.html',hasilfilter=hasilfilter,datagempa=datagempa)

@app.route('/graphic')
def graphic():
    return render_template('graphic.html')
