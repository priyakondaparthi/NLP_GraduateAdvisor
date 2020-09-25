import numpy as np
import os
from flask import Flask, request, jsonify, render_template
import pickle
import sqlite3
import db
import click
from flask import current_app, g
from flask.cli import with_appcontext




app = Flask(__name__,instance_path='/Users/priyankakondaparthi/Documents/Major Project - EE297/predict')
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'predict.sqlite'),
    )

try:
    os.makedirs(app.instance_path)
except OSError:
    pass
model = pickle.load(open('model.pkl', 'rb'))
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print("inside request ------------------------------------------------------------------")
    print(request.form.values)
    int_features = [str(x) for x in request.form.values()]

    print(int_features)

    if(len(int_features)>2 and len(int_features[1])==0):
        if(int_features[2]=="Submit"):
            like_context=db.get_db().execute('SELECT like_value,dislike_value from FEEDBACK').fetchall()
            print("printing like context",like_context[0]['like_value']+1)
            #comment
            db.get_db().execute('UPDATE  FEEDBACK set like_value=?',(like_context[0]['like_value']+1,))
            db.get_db().commit()
            
            return render_template('index1.html', like_count='{}'.format(like_context[0]['like_value']+1),dislike_count='{}'.format(like_context[0]['dislike_value']+1))
        if(int_features[2]=="Dislike"):
            like_context=db.get_db().execute('SELECT like_value,dislike_value from FEEDBACK').fetchall()
            print("printing like context",like_context[0]['dislike_value']+1)
            db.get_db().execute('UPDATE  FEEDBACK set dislike_value=?',(like_context[0]['dislike_value']+1,))
            db.get_db().commit()
            
            return render_template('index1.html', like_count='{}'.format(like_context[0]['like_value']+1),dislike_count='{}'.format(like_context[0]['dislike_value']+1))
    

    ## all ifs can be removed since we are querying with filter condition"
    # if(int_features[0]=='electives'):
    #     print("laddu")
    #     context_text="< You are only allowed to take one course outside the EE graduate courses.   if your overall or candidacy GPA is below  B+ (3.3), then this might lower your GPA you can convert EE295 to CR/NC. Up to 3 units of undergraduate upper-division courses taken in the EE Department at SJSU may be approved as electives, OR Up to 3 units graduate-level courses taken at SJSU but outside the Electrical Engineering Department may be approved as electives, OR Up to 6 units graduate-level Open University courses taken in the EE Department at SJSU (or transferred from another university before your admission to MSEE program at SJSU) may be approved as electives. The Department offers an opportunity to specialize in one of the areas of specialization: Logic/Digital/Embedded System Design, ASIC/VLSI Circuits, Analog/Mixed-Signal Integrated Circuits, Communications/Signal Processing/Machine Learning, Networking, Power Electronics and Control. A student can specialize in an area by taking at least 3 courses in that area. The electives can be taken from the area of specialization or from other areas. A student must consult his/her program advisor to design his/her program of study during the first semester in the department.>"
    # elif(int_features[0]=="graduation"):
    #     context_text="< To meet the requirements for the Master of Science Degree in Electrical Engineering, a student must complete 33 semester units with a cumulative major GPA of 3.0 or better, satisfy competency in written English for Graduate Students and the overall SJSU GPA is 3.0 or better. >"
    # elif(int_features[0]=="project"):
    #     context_text="<EE 297 (MSEE Project) or EE 299 (Master’s Thesis) is the culminating experience of the MSEE program and may therefore be taken after completing at least 12 units. Before a student is eligible to enroll in EE 297 or EE 299, he or she must have satisfied the CSU competency in written English requirement, filed the “Candidacy Form”. To register for EE297 or EE299, student must complete the appropriate form from and submit to the EE department for approval>"
    # elif(int_features[0]=="others"):
    #     context_text="< for course selection Please check ee.sjsu.edu . For graduate course advising please contact department graduate adviser Mrs. Birsen Sirkesi >"


    context_from_db=db.get_db().execute('SELECT context from post where category=?',(int_features[0],)).fetchall()
    to_predict = [{'context': context_from_db[0]['context'], 'qas': [{'question': int_features[1], 'id': '0'}]}]
    #final_features = [np.array(int_features)]
    prediction = model.predict(to_predict)
    
    output = prediction[0][0]['answer'][0]
    #output=2
    
    return render_template('index1.html', prediction_text='Your Answer: {}'.format(output), context=int_features[0],question=int_features[1])
    #return render_template('index.html', prediction_text='Your Answer: {}'.format(output), context=int_features[0],question=int_features[1])

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    
    #prediction = model.predict([np.array(list(data.values()))])
    print(data)
    #output = prediction[0]
    #return jsonify(output)
    return jsonify(data)

@app.route('/feedback',methods=['POST','GET'])
def feedback():
    #data = request.get_json(force=True)
    return render_template('index.html', prediction_text='Like')

if __name__ == "__main__":
    app.run(debug=True)