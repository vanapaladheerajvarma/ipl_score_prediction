from flask import Flask, render_template, request
import pickle
import numpy as np


filename = 'score-model.pkl'
regressor = pickle.load(open(filename, 'rb'))




app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/result',methods=["POST"])
def result():
        
                v=["Barabati Stadium","Brabourne Stadium","Buffalo Park","De Beers Diamond Oval","Dr DY Patil Sports Academy","Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", \
                "Dubai International Cricket Stadium","Eden Gardens","Feroz Shah Kotla", \
                "Himachal Pradesh Cricket Association Stadium","Holkar Cricket Stadium","JSCA International Stadium Complex","Kingsmead", \
                "M Chinnaswamy Stadium","MA Chidambaram Stadium, Chepauk","Maharashtra Cricket Association Stadium", \
                "New Wanderers Stadium","Newlands","OUTsurance Oval","Punjab Cricket Association IS Bindra Stadium, Mohali", \
                "Punjab Cricket Association Stadium, Mohali","Rajiv Gandhi International Stadium, Uppal","Sardar Patel Stadium, Motera", \
                "Sawai Mansingh Stadium","Shaheed Veer Narayan Singh International Stadium","Sharjah Cricket Stadium", \
                "Sheikh Zayed Stadium","St George's Park","Subrata Roy Sahara Stadium","SuperSport Park","Wankhede Stadium"]
                d1={}
                for i in v:
                    d1[i]=0
                venue= request.form["venue"]
                d1[venue]=1
                i1=list(d1.values())

                
                

                teams1=["Chennai Super Kings","Delhi Daredevils","Kings XI Punjab","Kolkata Knight Riders", \
                "Mumbai Indians","Rajasthan Royals","Royal Challengers Bangalore","Sunrisers Hyderabad"]
                d2={}
                for i in teams1:
                    d2[i]=0
                team1= request.form["team1"]
                d2[team1]=1
                i2=list(d2.values())
                


                d3={}
                for i in teams1:
                    d3[i]=0
                team2= request.form["team2"]
                d3[team2]=1
                i3=list(d3.values())

                overs= float(request.form["overs"])
                runs= int(request.form["runs"])
                wickets= int(request.form["wickets"])
                prev_runs= int(request.form["prev_runs"])
                prev_wickets= int(request.form["prev_wickets"])

                temp_array = [runs,wickets,overs,prev_runs,prev_wickets]+i1+i2+i3

                data=np.array([temp_array])

                prediction= int(regressor.predict(data)[0])
                
                return render_template('result.html',prediction=prediction,ve=venue,team1=team1,team2=team2)

                
    
        
                
            


            










app.run(debug=True)
