from flask import *
import joblib
import pickle
import gspread

# gc = gspread.service_account(filename = "cred.json")
# sh = gc.open_by_key("10Eaw0vi941eOeapiAVvfScrEySvWZBQiP_DmyPTUEfI")

# worksheet = sh.sheet1

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('rf_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/predict", methods = ['POST'])
def predict():
	if request.method == 'POST':
		
		state = int(request.form['state'])
		district = int(request.form['district'])
		crop = int(request.form['crop'])
		season = int(request.form['season'])
		field = float(request.form['field'])
		print(state,district,crop,season,field)
		
		prediction = model.predict([[state, district, crop, season, field]])
		print(prediction)
		out = prediction[0]
# 		if pred ==1:out = "Survived"
# 		else: out = "Didn't Survived"
			
# 		worksheet.append_row([name, out])
		return render_template('index.html', results = out)
	else:
		return render_template('index.html')		

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0')