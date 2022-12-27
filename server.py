import json
from flask import Flask , render_template,request,jsonify
import numpy as np
import pickle
import json


app = Flask(__name__)
heart_model = pickle.load(open('artifacts/heart/Heart.pkl', 'rb'))

kidney_model = pickle.load(open('artifacts/kidney/Kidney.pkl', 'rb'))

cancer_model = pickle.load(open('artifacts/breastCancer/Breast.pkl', 'rb'))


liver_model = pickle.load(open('artifacts/liver/Liver.pkl', 'rb'))

diabetes_model = pickle.load(open('artifacts/diabetes/Diabetes.pkl', 'rb'))

stroke_model = pickle.load(open('artifacts/stroke/Stroke.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/heart',methods=['GET'])
# def heart():
#     return render_template('heart_disease.html')

# @app.route('/heartdiseasepredict', methods=['POST'])
# @app.route('/api/heartdiseasepredict', methods=['POST'])
# def heart_predict():
#     if request.method == 'POST':
#         age = int(request.form['age'])
#         sex = int(request.form['sex'])
#         cp = int(request.form['cp'])
#         trestbps = int(request.form['trestbps'])
#         chol = int(request.form['chol'])
#         fbs = int(request.form['fbs'])
#         restecg = int(request.form['restecg'])
#         thalach = int(request.form['thalach'])
#         exang = float(request.form['exang'])
#         oldpeak = float(request.form['oldpeak'])
#         slope = int(request.form['slope'])
#         ca = int(request.form['ca'])
#         thal = int(request.form['thal'])
#         values = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
#         prediction = heart_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/heartdiseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='heart')

# @app.route('/kidney',methods=['GET'])
# def kidney():
#     return render_template('kidney_disease.html')

# @app.route("/kidneydiseasepredict", methods=['POST'])
# @app.route("/api/kidneydiseasepredict", methods=['POST'])
# def kidney_predict():
#     if request.method == 'POST':
#         sg = float(request.form['sg'])
#         htn = float(request.form['htn'])
#         hemo = float(request.form['hemo'])
#         dm = float(request.form['dm'])
#         al = float(request.form['al'])
#         appet = float(request.form['appet'])
#         rc = float(request.form['rc'])
#         pc = float(request.form['pc'])

#         values = np.array([[sg, htn, hemo, dm, al, appet, rc, pc]])
#         prediction = kidney_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/kidneydiseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='kidney')


# @app.route('/liver',methods=['GET'])
# def liver():
#     return render_template('liver_disease.html')

# @app.route("/liverdiseasepredict", methods=['POST'])
# @app.route("/api/liverdiseasepredict", methods=['POST'])
# def liver_predict():
#     if request.method == 'POST':
#         Age = int(request.form['Age'])
#         Gender = int(request.form['Gender'])
#         Total_Bilirubin = float(request.form['Total_Bilirubin'])
#         Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
#         Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
#         Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
#         Total_Protiens = float(request.form['Total_Protiens'])
#         Albumin = float(request.form['Albumin'])
#         Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])


#         values = np.array([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
#         prediction = liver_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/liverdiseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='liver')




# @app.route('/cancer', methods=['GET'])
# def cancer():
#     return render_template('cancer_disease.html')

# @app.route("/breastcancerdiseasepredict", methods=['POST'])
# @app.route("/api/breastcancerdiseasepredict", methods=['POST'])

# def cancer_predict():
#     if request.method == 'POST':
#         texture_mean = float(request.form['texture_mean'])
#         smoothness_mean = float(request.form['smoothness_mean'])
#         compactness_mean = float(request.form['compactness_mean'])
#         symmetry_mean = float(request.form['symmetry_mean'])
#         fractal_dimension_mean = float(request.form['fractal_dimension_mean'])
#         texture_se = float(request.form['texture_se'])
#         smoothness_se = float(request.form['smoothness_se'])
#         symmetry_se = float(request.form['symmetry_se'])
#         symmetry_worst = float(request.form['symmetry_worst'])

#         values = np.array([[texture_mean, smoothness_mean, compactness_mean, symmetry_mean, fractal_dimension_mean,
#                             texture_se, smoothness_se, symmetry_se, symmetry_worst]])
#         prediction = cancer_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/breastcancerdiseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='liver')


# @app.route('/diabetes',methods=['GET'])
# def diabebtes():
#     return render_template('diabetes_disease.html')

# @app.route("/diabetesdiseasepredict", methods=['POST'])
# @app.route("/api/diabetesdiseasepredict", methods=['POST'])
# def diabetes_predict():
#     if request.method == 'POST':
#         Pregnancies = int(request.form['Pregnancies'])
#         Glucose = int(request.form['Glucose'])
#         BloodPressure = int(request.form['BloodPressure'])
#         SkinThickness = int(request.form['SkinThickness'])
#         Insulin = int(request.form['Insulin'])
#         BMI = float(request.form['BMI'])
#         DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
#         Age = int(request.form['Age'])

#         values = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age]])
#         prediction = diabetes_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/diabetesdiseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='diabetes')

# @app.route('/stroke',methods=['GET'])
# def stroke():
#     return render_template('stroke_disease.html')


# @app.route("/strokediseasepredict", methods=['POST'])
# @app.route("/api/strokediseasepredict", methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         gender = request.form['gender']
#         if gender == 'Male':
#             gender_Male = 1
#             gender_Female = 0
#         else:
#             gender_Male = 0
#             gender_Female = 1

#         age = float(request.form['age'])
#         hypertension = int(request.form['hypertension'])
#         heart_disease = int(request.form['heart_disease'])
#         ever_married = int(request.form['ever_married'])
#         Residence_type = int(request.form['Residence_type'])
#         avg_glucose_level = float(request.form['avg_glucose_level'])
#         bmi = float(request.form['bmi'])


#         work_type = request.form['work_type']

#         if work_type == 'Never_worked':
#             work_type_Never_worked = 1
#             work_type_Private = 0
#             work_type_Self_employed = 0
#             work_type_children = 0
#             work_type_Govt_job = 0

#         if work_type == 'Private':
#             work_type_Never_worked = 0
#             work_type_Private = 1
#             work_type_Self_employed = 0
#             work_type_children = 0
#             work_type_Govt_job = 0

#         elif work_type == "Self_employed":
#             work_type_Never_worked = 0
#             work_type_Private = 0
#             work_type_Self_employed = 1
#             work_type_children = 0
#             work_type_Govt_job = 0

#         elif work_type == "children":
#             work_type_Never_worked = 0
#             work_type_Private = 0
#             work_type_Self_employed = 0
#             work_type_children = 1
#             work_type_Govt_job = 0

#         else:
#             work_type_Never_worked = 0
#             work_type_Private = 0
#             work_type_Self_employed = 0
#             work_type_children = 0
#             work_type_Govt_job = 1


#         smoking_status = request.form['smoking_status']

#         if smoking_status == "formerly_smoked":
#             smoking_status_formerly_smoked = 1
#             smoking_status_never_smoked = 0
#             smoking_status_Smokes = 0
#             smoking_status_Unknown = 0

#         elif smoking_status == "never_smoked":
#             smoking_status_formerly_smoked = 0
#             smoking_status_never_smoked = 1
#             smoking_status_Smokes = 0
#             smoking_status_Unknown = 0

#         elif smoking_status == "Smokes":
#             smoking_status_formerly_smoked = 0
#             smoking_status_never_smoked = 0
#             smoking_status_Smokes = 1
#             smoking_status_Unknown = 0

#         else:
#             smoking_status_formerly_smoked = 0
#             smoking_status_never_smoked = 0
#             smoking_status_Smokes = 0
#             smoking_status_Unknown = 1


#         values = np.array([[gender_Male,age, hypertension, heart_disease, ever_married,
#                             Residence_type, avg_glucose_level, bmi,
#                             work_type_Never_worked, work_type_Private,work_type_Self_employed, work_type_children,
#                             smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_Smokes]])
#         prediction = stroke_model.predict(values)
#         value = str(prediction)[1:-1]
#         response = jsonify({'heath': value})
        
#         if request.path == '/api/strokediseasepredict':
#             return response
#         return render_template('result.html', prediction=prediction,value='diabetes')


if __name__ == '__main__':
    print('Starting Python server')
    app.run()