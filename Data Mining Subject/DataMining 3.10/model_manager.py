import pickle

ml_models={
    "Decision Trees":"models/Decision Trees no SMOTE Model.sav",
    "Decision Trees with SMOTE":"models/Decision Trees SMOTE Model.sav",
    "KNN":"models/KNN no SMOTE Model.sav",
    "KNN with SMOTE":"models/KNN SMOTE Model.sav",
    "Logistic Regression":"models/Logistic Regression no SMOTE Model.sav",
    "Logistic Regression with SMOTE":"models/Logistic Regression SMOTE Model.sav",
    "Naive Bayes":"models/Naive Bayes no SMOTE Model.sav",
    "Naive Bayes with SMOTE":"models/Naive Bayes SMOTE Model.sav",
    "Random Forest":"models/Random Forest no SMOTE Model.sav",
    "Random Forest with SMOTE":"models/Random Forest SMOTE Model.sav",
    "SVM":"models/SVM no SMOTE Model.sav",
    "SVM with SMOTE":"models/SVM SMOTE Model.sav",
}

encoded_gender = {
    "male":1.0,
    "female":0.0
}

encoded_hypertension = {
    "yes":1.0,
    "no":0.0
}

encoded_heart_disease = {
    "yes":1.0,
    "no":0.0
}

encoded_married = {
    "yes":1.0,
    "no":0.0
}

encoded_work_type = {
    "Govt_job":0.0,
    "never_worked":1.0,
    "Private":2.0,
    "Self Employed":3.0,
    "Children":4.0,
}

encoded_residence = {
    "Urban":1.0,
    "Rural":0.0
}

encoded_smoking_status = {
    "formerly smoked":0.0,
    "never smoked":1.0,
    "smokes":2.0,
}


available_models = list(ml_models.keys())
for model_name in available_models:
    print(model_name)
selected = input("Please select a model from the list above:")

if selected in ml_models:
    model_file_path = ml_models[selected]
    model = pickle.load(open(model_file_path,"rb"))
    print("model '"+selected+"' successfully loaded!")
    print("======Patient Information======")
    
    print("patient sex options:")
    for option in encoded_gender:
        print(option)
    gender=input("patient sex:")
    
    age=float(input("patient age:"))

    print("patient hypertension options:")
    for option in encoded_hypertension:
        print(option)
    hypertension=input("patient hypertension:")
    
    print("patient heart disease options:")
    for option in encoded_heart_disease:
        print(option)
    heart_disease=input("patient heart disease:")
    
    print("patient marriage status options:")
    for option in encoded_married:
        print(option)
    ever_married=input("patient marriage status:")
    
    print("patient work type options:")
    for option in encoded_work_type:
        print(option)
    work_type=input("patient work type:")
    
    print("patient residence type options:")
    for option in encoded_residence:
        print(option)
    residence_type=input("patient residence type:")
    
    avg_glucose_level=float(input("patient average glucose level:"))
    
    bmi=float(input("patient BMI:"))
    
    print("patient smoking status options:")
    for option in encoded_smoking_status:
        print(option)
    smoking_status=input("patient smoking status:")

    print(gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status)
    gender=encoded_gender[gender]
    hypertension=encoded_hypertension[hypertension]
    heart_disease=encoded_heart_disease[heart_disease]
    ever_married=encoded_married[ever_married]
    work_type=encoded_work_type[work_type]
    residence_type=encoded_residence[residence_type]
    smoking_status=encoded_smoking_status[smoking_status]
    print(gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status)
    
    answer = model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,residence_type,avg_glucose_level,bmi,smoking_status]])
    if answer == 1:
        print("\nPatient had a stroke")
    elif answer == 0:
        print("\nPatient had no stroke")

else:
    print("model '"+selected+"' cannot be found!")
