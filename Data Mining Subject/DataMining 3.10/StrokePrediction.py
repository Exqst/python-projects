# Authors:
# Flores, Joash Edson E.
# Gatdula, Raymond Christian P.
# Elequin, Carlos Joshua G.
# BSCS4-4
# Data Mining
# Final Project

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QValidator, QIntValidator, QDoubleValidator
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
    "Male":1.0,
    "Female":0.0,
    "Others":2.0,

}

encoded_hypertension = {
    "Yes":1.0,
    "No":0.0,

}

encoded_heart_disease = {
    "Yes":1.0,
    "No":0.0,

}

encoded_married = {
    "Yes":1.0,
    "No":0.0,

}

encoded_work_type = {
    "Govt_Job":0.0,
    "Never_Worked":1.0,
    "Private":2.0,
    "Self-Employed":3.0,
    "Children":4.0,

}

encoded_residence = {
    "Urban":1.0,
    "Rural":0.0,

}

encoded_smoking_status = {
    "Formerly_Smoked":0.0,
    "Never_Smoked":1.0,
    "Smokes":2.0,

}

class Ui_Error_Window(object):
    def MainMenu(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Main_StrokePrediction()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, Error_Window):
        Error_Window.setObjectName("Error_Window")
        Error_Window.resize(240, 161)
        self.centralwidget = QtWidgets.QWidget(Error_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ErrorOkay = QtWidgets.QPushButton(self.centralwidget)
        self.ErrorOkay.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.ErrorOkay.setObjectName("ErrorOkay")
        self.ErrorOkay.clicked.connect(self.MainMenu)
        self.ErrorOkay.clicked.connect(Error_Window.close)
        Error_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Error_Window)
        self.statusbar.setObjectName("statusbar")
        Error_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Error_Window)
        QtCore.QMetaObject.connectSlotsByName(Error_Window)

    def retranslateUi(self, Error_Window):
        _translate = QtCore.QCoreApplication.translate
        Error_Window.setWindowTitle(_translate("Error_Window", "Error"))
        self.label.setText(_translate("Error_Window", "Please Complete the Form."))
        self.ErrorOkay.setText(_translate("Error_Window", "Okay"))
        
class Ui_AlertBoxNo(object):
    def MainMenu(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Main_StrokePrediction()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        
    def setupUi(self, AlertBoxNo):
        AlertBoxNo.setObjectName("AlertBoxNo")
        AlertBoxNo.resize(319, 401)
        self.centralwidget = QtWidgets.QWidget(AlertBoxNo)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 10, 201, 282))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.NoAlgorithmLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoAlgorithmLabel.setObjectName("NoAlgorithmLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NoAlgorithmLabel)
        self.NoAlgorithmLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoAlgorithmLineEdit.setEnabled(False)
        self.NoAlgorithmLineEdit.setObjectName("NoAlgorithmLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NoAlgorithmLineEdit)
        self.NoGenderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoGenderLabel.setObjectName("NoGenderLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NoGenderLabel)
        self.NoGenderLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoGenderLineEdit.setEnabled(False)
        self.NoGenderLineEdit.setObjectName("NoGenderLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NoGenderLineEdit)
        self.NoAgeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoAgeLabel.setObjectName("NoAgeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.NoAgeLabel)
        self.NoAgeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoAgeLineEdit.setEnabled(False)
        self.NoAgeLineEdit.setObjectName("NoAgeLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.NoAgeLineEdit)
        self.NoHyperTensionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoHyperTensionLabel.setObjectName("NoHyperTensionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.NoHyperTensionLabel)
        self.NoHyperTensionLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoHyperTensionLineEdit.setEnabled(False)
        self.NoHyperTensionLineEdit.setObjectName("NoHyperTensionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.NoHyperTensionLineEdit)
        self.NoHeartDiseaseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoHeartDiseaseLabel.setObjectName("NoHeartDiseaseLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.NoHeartDiseaseLabel)
        self.NoHeartDiseaseLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoHeartDiseaseLineEdit.setEnabled(False)
        self.NoHeartDiseaseLineEdit.setObjectName("NoHeartDiseaseLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.NoHeartDiseaseLineEdit)
        self.NoEverMarriedLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoEverMarriedLabel.setObjectName("NoEverMarriedLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.NoEverMarriedLabel)
        self.NoEverMarriedLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoEverMarriedLineEdit.setEnabled(False)
        self.NoEverMarriedLineEdit.setObjectName("NoEverMarriedLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.NoEverMarriedLineEdit)
        self.NoWorkTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoWorkTypeLabel.setObjectName("NoWorkTypeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.NoWorkTypeLabel)
        self.NoWorkTypeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoWorkTypeLineEdit.setEnabled(False)
        self.NoWorkTypeLineEdit.setObjectName("NoWorkTypeLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.NoWorkTypeLineEdit)
        self.NoResidenceTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoResidenceTypeLabel.setObjectName("NoResidenceTypeLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.NoResidenceTypeLabel)
        self.NoResidenceTypeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoResidenceTypeLineEdit.setEnabled(False)
        self.NoResidenceTypeLineEdit.setObjectName("NoResidenceTypeLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.NoResidenceTypeLineEdit)
        self.NoGlucoseLevelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoGlucoseLevelLabel.setObjectName("NoGlucoseLevelLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.NoGlucoseLevelLabel)
        self.NoGlucoseLevelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoGlucoseLevelLineEdit.setEnabled(False)
        self.NoGlucoseLevelLineEdit.setObjectName("NoGlucoseLevelLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.NoGlucoseLevelLineEdit)
        self.NoBodyMassIndexLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoBodyMassIndexLabel.setObjectName("NoBodyMassIndexLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.NoBodyMassIndexLabel)
        self.NoBodyMassIndexLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoBodyMassIndexLineEdit.setEnabled(False)
        self.NoBodyMassIndexLineEdit.setObjectName("NoBodyMassIndexLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.NoBodyMassIndexLineEdit)
        self.NoSmokingStatusLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.NoSmokingStatusLabel.setObjectName("NoSmokingStatusLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.NoSmokingStatusLabel)
        self.NoSmokingStatusLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.NoSmokingStatusLineEdit.setEnabled(False)
        self.NoSmokingStatusLineEdit.setObjectName("NoSmokingStatusLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.NoSmokingStatusLineEdit)
        self.NoOkayButton = QtWidgets.QPushButton(self.centralwidget)
        self.NoOkayButton.setGeometry(QtCore.QRect(100, 340, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NoOkayButton.setFont(font)
        self.NoOkayButton.setObjectName("NoOkayButton")
        self.NoOkayButton.clicked.connect(self.MainMenu)
        self.NoOkayButton.clicked.connect(AlertBoxNo.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 310, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        AlertBoxNo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AlertBoxNo)
        self.statusbar.setObjectName("statusbar")
        AlertBoxNo.setStatusBar(self.statusbar)

        self.retranslateUi(AlertBoxNo)
        QtCore.QMetaObject.connectSlotsByName(AlertBoxNo)

    def retranslateUi(self, AlertBoxNo):
        _translate = QtCore.QCoreApplication.translate
        AlertBoxNo.setWindowTitle(_translate("AlertBoxNo", "Stroke Prediction"))
        self.NoAlgorithmLabel.setText(_translate("AlertBoxNo", "Algorithm"))
        self.NoGenderLabel.setText(_translate("AlertBoxNo", "Gender"))
        self.NoAgeLabel.setText(_translate("AlertBoxNo", "Age"))
        self.NoHyperTensionLabel.setText(_translate("AlertBoxNo", "Hyper Tension"))
        self.NoHeartDiseaseLabel.setText(_translate("AlertBoxNo", "Heart Disease"))
        self.NoEverMarriedLabel.setText(_translate("AlertBoxNo", "Ever Married"))
        self.NoWorkTypeLabel.setText(_translate("AlertBoxNo", "Work Type"))
        self.NoResidenceTypeLabel.setText(_translate("AlertBoxNo", "Residence Type"))
        self.NoGlucoseLevelLabel.setText(_translate("AlertBoxNo", "Glucose Level"))
        self.NoBodyMassIndexLabel.setText(_translate("AlertBoxNo", "Body Mass Index"))
        self.NoSmokingStatusLabel.setText(_translate("AlertBoxNo", "Smoking Status"))
        self.NoOkayButton.setText(_translate("AlertBoxNo", "Okay"))
        self.label.setText(_translate("AlertBoxNo", "You're not likely to have a stroke."))

class Ui_AlertBoxYes(object):
    def MainMenu(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Main_StrokePrediction()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, AlertBoxYes):
        AlertBoxYes.setObjectName("AlertBoxYes")
        AlertBoxYes.resize(318, 393)
        self.centralwidget = QtWidgets.QWidget(AlertBoxYes)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 10, 201, 282))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.YesAlgorithmLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesAlgorithmLabel.setObjectName("YesAlgorithmLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.YesAlgorithmLabel)
        self.algorithmLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.algorithmLineEdit.setEnabled(False)
        self.algorithmLineEdit.setObjectName("algorithmLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.algorithmLineEdit)
        self.YesGenderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesGenderLabel.setObjectName("YesGenderLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.YesGenderLabel)
        self.genderLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.genderLineEdit.setEnabled(False)
        self.genderLineEdit.setObjectName("genderLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.genderLineEdit)
        self.YesAgeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesAgeLabel.setObjectName("YesAgeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.YesAgeLabel)
        self.ageLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ageLineEdit.setEnabled(False)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ageLineEdit)
        self.YesHyperTensionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesHyperTensionLabel.setObjectName("YesHyperTensionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.YesHyperTensionLabel)
        self.hyperTensionLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.hyperTensionLineEdit.setEnabled(False)
        self.hyperTensionLineEdit.setObjectName("hyperTensionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hyperTensionLineEdit)
        self.YesHeartDiseaseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesHeartDiseaseLabel.setObjectName("YesHeartDiseaseLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.YesHeartDiseaseLabel)
        self.heartDiseaseLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.heartDiseaseLineEdit.setEnabled(False)
        self.heartDiseaseLineEdit.setObjectName("heartDiseaseLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.heartDiseaseLineEdit)
        self.YesEverMarriedLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesEverMarriedLabel.setObjectName("YesEverMarriedLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.YesEverMarriedLabel)
        self.everMarriedLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.everMarriedLineEdit.setEnabled(False)
        self.everMarriedLineEdit.setObjectName("everMarriedLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.everMarriedLineEdit)
        self.YesWorkTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesWorkTypeLabel.setObjectName("YesWorkTypeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.YesWorkTypeLabel)
        self.workTypeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.workTypeLineEdit.setEnabled(False)
        self.workTypeLineEdit.setObjectName("workTypeLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.workTypeLineEdit)
        self.YesresidenceTypeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesresidenceTypeLabel.setObjectName("YesresidenceTypeLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.YesresidenceTypeLabel)
        self.residenceTypeLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.residenceTypeLineEdit.setEnabled(False)
        self.residenceTypeLineEdit.setObjectName("residenceTypeLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.residenceTypeLineEdit)
        self.YesGlucoseLevelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesGlucoseLevelLabel.setObjectName("YesGlucoseLevelLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.YesGlucoseLevelLabel)
        self.glucoseLevelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.glucoseLevelLineEdit.setEnabled(False)
        self.glucoseLevelLineEdit.setObjectName("glucoseLevelLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.glucoseLevelLineEdit)
        self.YesBodyMassIndexLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesBodyMassIndexLabel.setObjectName("YesBodyMassIndexLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.YesBodyMassIndexLabel)
        self.bodyMassIndexLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bodyMassIndexLineEdit.setEnabled(False)
        self.bodyMassIndexLineEdit.setObjectName("bodyMassIndexLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.bodyMassIndexLineEdit)
        self.YesSmokingStatusLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.YesSmokingStatusLabel.setObjectName("YesSmokingStatusLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.YesSmokingStatusLabel)
        self.smokingStatusLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.smokingStatusLineEdit.setEnabled(False)
        self.smokingStatusLineEdit.setObjectName("smokingStatusLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.smokingStatusLineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 310, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 340, 81, 31))
        self.pushButton.clicked.connect(self.MainMenu)
        self.pushButton.clicked.connect(AlertBoxYes.close)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        AlertBoxYes.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AlertBoxYes)
        self.statusbar.setObjectName("statusbar")
        AlertBoxYes.setStatusBar(self.statusbar)

        self.retranslateUi(AlertBoxYes)
        QtCore.QMetaObject.connectSlotsByName(AlertBoxYes)

    def retranslateUi(self, AlertBoxYes):
        _translate = QtCore.QCoreApplication.translate
        AlertBoxYes.setWindowTitle(_translate("AlertBoxYes", "Stroke Prediction"))
        self.YesAlgorithmLabel.setText(_translate("AlertBoxYes", "Algorithm"))
        self.YesGenderLabel.setText(_translate("AlertBoxYes", "Gender"))
        self.YesAgeLabel.setText(_translate("AlertBoxYes", "Age"))
        self.YesHyperTensionLabel.setText(_translate("AlertBoxYes", "Hyper Tension"))
        self.YesHeartDiseaseLabel.setText(_translate("AlertBoxYes", "Heart Disease"))
        self.YesEverMarriedLabel.setText(_translate("AlertBoxYes", "Ever Married"))
        self.YesWorkTypeLabel.setText(_translate("AlertBoxYes", "Work Type"))
        self.YesresidenceTypeLabel.setText(_translate("AlertBoxYes", "Residence Type"))
        self.YesGlucoseLevelLabel.setText(_translate("AlertBoxYes", "Glucose Level"))
        self.YesBodyMassIndexLabel.setText(_translate("AlertBoxYes", "Body Mass Index"))
        self.YesSmokingStatusLabel.setText(_translate("AlertBoxYes", "Smoking Status"))
        self.label.setText(_translate("AlertBoxYes", "You're most likely to have a stroke."))
        self.pushButton.setText(_translate("AlertBoxYes", "Okay"))

        
class Ui_Main_StrokePrediction(object):
    def AlertYes(self) :
        self.YesWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AlertBoxYes()
        self.ui.setupUi (self.YesWindow)
        self.YesWindow.show()
        
    def AlertNo(self):
        self.NoWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AlertBoxNo()
        self.ui.setupUi(self.NoWindow)
        self.NoWindow.show()
        
    def Error(self):
        self.ErrorWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Error_Window()
        self.ui.setupUi (self.ErrorWindow)
        self.ErrorWindow.show()
    
    def setupUi(self, Main_StrokePrediction):
        Main_StrokePrediction.setObjectName("Main_StrokePrediction")
        Main_StrokePrediction.resize(575, 401)
        Main_StrokePrediction.setAutoFillBackground(True)
        self.WindowNo = Ui_AlertBoxNo()
        self.WindowYes = Ui_AlertBoxYes()
        self.WindowError = Ui_Error_Window()
        self.Validator = QIntValidator()
        self.GlucoseValidator = QDoubleValidator(0, 271.74, 2, None)
        self.BMIValidator = QDoubleValidator(0,92,2,None)
        self.PredictButton = QtWidgets.QPushButton(Main_StrokePrediction)
        self.PredictButton.setGeometry(QtCore.QRect(230, 310, 111, 41))
        self.PredictButton.clicked.connect(self.ValueGetter)
        self.PredictButton.clicked.connect(Main_StrokePrediction.close)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PredictButton.setFont(font)
        self.PredictButton.setObjectName("PredictButton")
        self.gridLayoutWidget = QtWidgets.QWidget(Main_StrokePrediction)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 140, 231, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.LeftForm = QtWidgets.QFormLayout(self.gridLayoutWidget)
        self.LeftForm.setContentsMargins(0, 0, 0, 0)
        self.LeftForm.setObjectName("LeftForm")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.LeftForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.GenderComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.GenderComboBox.setObjectName("GenderComboBox")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.LeftForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.GenderComboBox)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.LeftForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.AgeText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.AgeText.setValidator(self.Validator)
        self.AgeText.setText("")
        self.AgeText.setObjectName("AgeText")
        self.LeftForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AgeText)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LeftForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.HyperTensionComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.HyperTensionComboBox.setObjectName("HyperTensionComboBox")
        self.HyperTensionComboBox.addItem("")
        self.HyperTensionComboBox.addItem("")
        self.HyperTensionComboBox.addItem("")
        self.LeftForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.HyperTensionComboBox)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.LeftForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.HeartDiseaseComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.HeartDiseaseComboBox.setObjectName("HeartDiseaseComboBox")
        self.HeartDiseaseComboBox.addItem("")
        self.HeartDiseaseComboBox.addItem("")
        self.HeartDiseaseComboBox.addItem("")
        self.LeftForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.HeartDiseaseComboBox)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.LeftForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.EverMarriedCombobox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.EverMarriedCombobox.setObjectName("EverMarriedCombobox")
        self.EverMarriedCombobox.addItem("")
        self.EverMarriedCombobox.addItem("")
        self.EverMarriedCombobox.addItem("")
        self.LeftForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.EverMarriedCombobox)
        self.formLayoutWidget = QtWidgets.QWidget(Main_StrokePrediction)
        self.formLayoutWidget.setGeometry(QtCore.QRect(320, 140, 244, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.RightForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.RightForm.setContentsMargins(0, 0, 0, 0)
        self.RightForm.setObjectName("RightForm")
        self.WorkTypeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.WorkTypeComboBox.setObjectName("WorkTypeComboBox")
        self.WorkTypeComboBox.addItem("")
        self.WorkTypeComboBox.addItem("")
        self.WorkTypeComboBox.addItem("")
        self.WorkTypeComboBox.addItem("")
        self.WorkTypeComboBox.addItem("")
        self.WorkTypeComboBox.addItem("")
        self.RightForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.WorkTypeComboBox)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.RightForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ResidenceTypeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ResidenceTypeComboBox.setObjectName("ResidenceTypeComboBox")
        self.ResidenceTypeComboBox.addItem("")
        self.ResidenceTypeComboBox.addItem("")
        self.ResidenceTypeComboBox.addItem("")
        self.RightForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ResidenceTypeComboBox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.RightForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.GlucoseLevelText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.GlucoseLevelText.setValidator(self.GlucoseValidator)
        self.GlucoseLevelText.setObjectName("GlucoseLevelText")
        self.RightForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.GlucoseLevelText)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.RightForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.BMIText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.BMIText.setValidator(self.BMIValidator)
        self.BMIText.setObjectName("BMIText")
        self.RightForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BMIText)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.RightForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.SmokingStatusComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.SmokingStatusComboBox.setObjectName("SmokingStatusComboBox")
        self.SmokingStatusComboBox.addItem("")
        self.SmokingStatusComboBox.addItem("")
        self.SmokingStatusComboBox.addItem("")
        self.SmokingStatusComboBox.addItem("")
        self.RightForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.SmokingStatusComboBox)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.RightForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label = QtWidgets.QLabel(Main_StrokePrediction)
        self.label.setGeometry(QtCore.QRect(140, 30, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AlgorithmComboBox = QtWidgets.QComboBox(Main_StrokePrediction)
        self.AlgorithmComboBox.setGeometry(QtCore.QRect(290, 90, 190, 22))
        self.AlgorithmComboBox.setObjectName("AlgorithmComboBox")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.AlgorithmComboBox.addItem("")
        self.label_12 = QtWidgets.QLabel(Main_StrokePrediction)
        self.label_12.setGeometry(QtCore.QRect(140, 90, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Main_StrokePrediction)
        QtCore.QMetaObject.connectSlotsByName(Main_StrokePrediction)

    def retranslateUi(self, Main_StrokePrediction):
        _translate = QtCore.QCoreApplication.translate
        Main_StrokePrediction.setWindowTitle(_translate("Main_StrokePrediction", "Stroke Prediction"))
        self.PredictButton.setText(_translate("Main_StrokePrediction", "Predict"))
        self.label_2.setText(_translate("Main_StrokePrediction", "Gender:"))
        self.GenderComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.GenderComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.GenderComboBox.setItemText(1, _translate("Main_StrokePrediction", "Male"))
        self.GenderComboBox.setItemText(2, _translate("Main_StrokePrediction", "Female"))
        self.GenderComboBox.setItemText(3, _translate("Main_StrokePrediction", "Others"))
        self.label_3.setText(_translate("Main_StrokePrediction", "Age:"))
        self.label_4.setText(_translate("Main_StrokePrediction", "Hyper Tension:"))
        self.HyperTensionComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.HyperTensionComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.HyperTensionComboBox.setItemText(1, _translate("Main_StrokePrediction", "Yes"))
        self.HyperTensionComboBox.setItemText(2, _translate("Main_StrokePrediction", "No"))
        self.label_5.setText(_translate("Main_StrokePrediction", "Heart Disease: "))
        self.HeartDiseaseComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.HeartDiseaseComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.HeartDiseaseComboBox.setItemText(1, _translate("Main_StrokePrediction", "Yes"))
        self.HeartDiseaseComboBox.setItemText(2, _translate("Main_StrokePrediction", "No"))
        self.label_6.setText(_translate("Main_StrokePrediction", "Ever Married:"))
        self.EverMarriedCombobox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.EverMarriedCombobox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.EverMarriedCombobox.setItemText(1, _translate("Main_StrokePrediction", "Yes"))
        self.EverMarriedCombobox.setItemText(2, _translate("Main_StrokePrediction", "No"))
        self.WorkTypeComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.WorkTypeComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.WorkTypeComboBox.setItemText(1, _translate("Main_StrokePrediction", "Never_Worked"))
        self.WorkTypeComboBox.setItemText(2, _translate("Main_StrokePrediction", "Self-Employed"))
        self.WorkTypeComboBox.setItemText(3, _translate("Main_StrokePrediction", "Private"))
        self.WorkTypeComboBox.setItemText(4, _translate("Main_StrokePrediction", "Govt_Job"))
        self.WorkTypeComboBox.setItemText(5, _translate("Main_StrokePrediction", "Children"))
        self.label_8.setText(_translate("Main_StrokePrediction", "Residence Type:"))
        self.ResidenceTypeComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.ResidenceTypeComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.ResidenceTypeComboBox.setItemText(1, _translate("Main_StrokePrediction", "Rural"))
        self.ResidenceTypeComboBox.setItemText(2, _translate("Main_StrokePrediction", "Urban"))
        self.label_9.setText(_translate("Main_StrokePrediction", "Glucose Level:"))
        self.label_10.setText(_translate("Main_StrokePrediction", "Body Mass Index:"))
        self.label_11.setText(_translate("Main_StrokePrediction", "Smoking Status:"))
        self.SmokingStatusComboBox.setCurrentText(_translate("Main_StrokePrediction", "--"))
        self.SmokingStatusComboBox.setItemText(0, _translate("Main_StrokePrediction", "--"))
        self.SmokingStatusComboBox.setItemText(1, _translate("Main_StrokePrediction", "Formerly_Smoked"))
        self.SmokingStatusComboBox.setItemText(2, _translate("Main_StrokePrediction", "Never_Smoked"))
        self.SmokingStatusComboBox.setItemText(3, _translate("Main_StrokePrediction", "Smokes"))
        self.label_7.setText(_translate("Main_StrokePrediction", "Work Type:"))
        self.label.setText(_translate("Main_StrokePrediction", "Stroke Prediction"))
        self.AlgorithmComboBox.setCurrentText(_translate("Main_StrokePrediction", "Decision Trees"))
        self.AlgorithmComboBox.setItemText(0, _translate("Main_StrokePrediction", "Decision Trees"))
        self.AlgorithmComboBox.setItemText(1, _translate("Main_StrokePrediction", "Decision Trees with SMOTE"))
        self.AlgorithmComboBox.setItemText(2, _translate("Main_StrokePrediction", "KNN"))
        self.AlgorithmComboBox.setItemText(3, _translate("Main_StrokePrediction", "KNN with SMOTE"))
        self.AlgorithmComboBox.setItemText(4, _translate("Main_StrokePrediction", "Logistic Regression"))
        self.AlgorithmComboBox.setItemText(5, _translate("Main_StrokePrediction", "Logistic Regression with SMOTE"))
        self.AlgorithmComboBox.setItemText(6, _translate("Main_StrokePrediction", "Naive Bayes"))
        self.AlgorithmComboBox.setItemText(7, _translate("Main_StrokePrediction", "Naive Bayes with SMOTE"))
        self.AlgorithmComboBox.setItemText(8, _translate("Main_StrokePrediction", "Random Forest"))
        self.AlgorithmComboBox.setItemText(9, _translate("Main_StrokePrediction", "Random Forest with SMOTE"))
        self.AlgorithmComboBox.setItemText(10, _translate("Main_StrokePrediction", "SVM"))
        self.AlgorithmComboBox.setItemText(11, _translate("Main_StrokePrediction", "SVM with SMOTE"))
        self.label_12.setText(_translate("Main_StrokePrediction", "Select Algorithm"))
        
    def ValueGetter(self):
        setAge = int(self.AgeText.text())
        setGlucose = float(self.GlucoseLevelText.text())
        setBMI = float(self.BMIText.text())
        setGender = self.GenderComboBox.currentText()
        setAlgo = self.AlgorithmComboBox.currentText()
        setHTension = self.HyperTensionComboBox.currentText()
        setHDisease = self.HeartDiseaseComboBox.currentText()
        setMarried = self.EverMarriedCombobox.currentText()
        setWork = self.WorkTypeComboBox.currentText()
        setResidence = self.ResidenceTypeComboBox.currentText()
        setSmoke = self.SmokingStatusComboBox.currentText()
                
        #Incomplete inputs
        if (setAge == "" 
            or setGlucose == ""
            or setBMI == ""
            or setGender == "--"
            or setHTension == "--"
            or setHDisease == "--"
            or setMarried == "--"
            or setWork == "--"
            or setResidence == "--"
            or setSmoke == "--"
            ):
            self.Error()
                
        #Checker for selected algorithm
        if setAlgo in ml_models:
            model_file_path = ml_models[setAlgo]
            model = pickle.load(open(model_file_path,"rb"))
            print("model '"+setAlgo+"' successfully loaded!")
            
            gender = setGender
            age = setAge
            hypertension = setHTension
            heartDisease = setHDisease
            married = setMarried
            worktype = setWork
            residency = setResidence
            Glucose = float(setGlucose)
            NewBMI = float(setBMI)
            SmokingStatus = setSmoke
            #Checker to see if the values from the UI is acquired
            print(gender, age, hypertension, heartDisease, married, worktype, residency, Glucose, NewBMI, SmokingStatus)
            #Converts to 0 and 1 so that the model can predict
            gender=encoded_gender[gender]
            hypertension=encoded_hypertension[hypertension]
            heartDisease=encoded_heart_disease[heartDisease]
            married=encoded_married[married]
            worktype=encoded_work_type[worktype]
            residency=encoded_residence[residency]
            SmokingStatus=encoded_smoking_status[SmokingStatus]
            #Checker to see if the encoding works
            print(gender, age, hypertension, heartDisease, married, worktype, residency, Glucose, NewBMI, SmokingStatus)
            
            answer = model.predict([[gender,age,hypertension,heartDisease,married,worktype,residency,Glucose,NewBMI,SmokingStatus]])
            if answer == 1:
                self.AlertYes()
                self.ui.algorithmLineEdit.setText(setAlgo)
                self.ui.ageLineEdit.setText(str(setAge))
                self.ui.bodyMassIndexLineEdit.setText(str(setBMI))
                self.ui.everMarriedLineEdit.setText(setMarried)
                self.ui.genderLineEdit.setText(setGender)
                self.ui.hyperTensionLineEdit.setText(setHTension)
                self.ui.heartDiseaseLineEdit.setText(setHDisease)
                self.ui.workTypeLineEdit.setText(setWork)
                self.ui.residenceTypeLineEdit.setText(setResidence)
                self.ui.glucoseLevelLineEdit.setText(str(setGlucose))
                self.ui.smokingStatusLineEdit.setText(setSmoke)
                setAge = ""
                setGlucose = ""
                setBMI = ""
                setGender = "--"
                setHTension = "--"
                setHDisease = "--"
                setMarried = "--"
                setWork = "--"
                setResidence = "--"
                setSmoke = "--"
            elif answer == 0:
                self.AlertNo()
                self.ui.NoAlgorithmLineEdit.setText(setAlgo)
                self.ui.NoAgeLineEdit.setText(str(setAge))
                self.ui.NoBodyMassIndexLineEdit.setText(str(setBMI))
                self.ui.NoEverMarriedLineEdit.setText(setMarried)
                self.ui.NoGenderLineEdit.setText(setGender)
                self.ui.NoHyperTensionLineEdit.setText(setHTension)
                self.ui.NoHeartDiseaseLineEdit.setText(setHDisease)
                self.ui.NoWorkTypeLineEdit.setText(setWork)
                self.ui.NoResidenceTypeLineEdit.setText(setResidence)
                self.ui.NoGlucoseLevelLineEdit.setText(str(setGlucose))
                self.ui.NoSmokingStatusLineEdit.setText(setSmoke)
                setAge = ""
                setGlucose = ""
                setBMI = ""
                setGender = "--"
                setHTension = "--"
                setHDisease = "--"
                setMarried = "--"
                setWork = "--"
                setResidence = "--"
                setSmoke = "--"
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_StrokePrediction = QtWidgets.QDialog()
    ui = Ui_Main_StrokePrediction()
    ui.setupUi(Main_StrokePrediction)
    Main_StrokePrediction.show()
    sys.exit(app.exec_())