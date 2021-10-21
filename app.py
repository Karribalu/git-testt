# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
from flask import Flask, request, jsonify,render_template
import joblib
import pandas as pd
import numpy as np
app = Flask(__name__,static_url_path='/static')

model = joblib.load('RandomForest3.pkl')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict', methods=['GET','POST'])
def Random():
    S_GENDER = ''
    S_LOCALE_VAL = ''
    S_STATE_VAL = ''
    S_CLIENT_CD = ''
    S_TRANS_STATUS = ''
    S_TRANS_METHOD = ''
    S_SUB_PRODUCT_CD = ''
    S_AMOUNT_I = ''
    S_AGE_I = ''
    model = joblib.load("RandomForest3.pkl")
    print(request.form)
  
    AMOUNT=int(request.form['AMOUNT'])
    print(AMOUNT)
    
    if(AMOUNT > 0 and AMOUNT <= 207500 ):
        S_AMOUNT_I = 0
    elif(AMOUNT > 207500 and AMOUNT <= 415000):
        S_AMOUNT_I = 1
    elif(AMOUNT > 415000 and AMOUNT <= 622500 ):
        S_AMOUNT_I = 2
    else:
        S_AMOUNT_I = 3
        
    AGE = int(request.form['AGE'])
    if(AGE > 0 and AGE <= 30):
        S_AGE_I = 0
    elif(AGE > 30 and AGE <= 45):
        S_AGE_I = 1
    elif(AGE > 45 and AGE <= 60):
        S_AGE_I = 2
    else:
        S_AGE_I = 3
    
    GENDER = request.form['GENDER']
    if(GENDER == 'Male'):
        S_GENDER = 1
    else:
        S_GENDER = 0
    
    
    print(GENDER)
    LOCALE_VAL = request.form['LOCALE_VAL']
    print(LOCALE_VAL)
    if(LOCALE_VAL == 'en_US'):
        S_LOCALE_VAL = 0
    else:
        S_LOCALE_VAL = 1
        
        
    SOURCE = request.form['SOURCE']
    if(SOURCE == 'VGRO'):
        S_SOURCE = 0
    elif(SOURCE == 'WEB'):
        S_SOURCE = 1
    else:
        S_SOURCE = 2
    
    print(SOURCE)

    
    STATE_VAL = request.form['STATE_VAL']
    if(STATE_VAL =='Other'):
        S_STATE_VAL = 0
        
    elif(STATE_VAL =='ST_VIET_1'):
        S_STATE_VAL = 1
            
            
    elif(STATE_VAL =='ST_VIET_2'):
        S_STATE_VAL = 2
            
    elif(STATE_VAL =='ST_VIET_3'):
        S_STATE_VAL = 3
            
    elif(STATE_VAL == 'ST_VIET_4'):
        S_STATE_VAL = 4
            
    elif(STATE_VAL =='ST_VIET_5'):
        S_STATE_VAL = 5
            
    elif(STATE_VAL =='ST_VIET_6'):
        S_STATE_VAL = 6
            
    elif(STATE_VAL =='ST_VIET_7'):
        S_STATE_VAL = 7
            
    elif(STATE_VAL =='ST_VIET_8'):
        S_STATE_VAL = 8
            
    elif(STATE_VAL =='ST_VIET_9'):
        S_STATE_VAL = 9
            
    elif(STATE_VAL == 'ST_VIET_10'):
        S_STATE_VAL = 10
            
    elif(STATE_VAL =='ST_VIET_11'):
        S_STATE_VAL = 11
            
    elif(STATE_VAL =='ST_VIET_12'):
        S_STATE_VAL = 12
        
    elif(STATE_VAL =='ST_VIET_13'):
        S_STATE_VAL = 13
            
    elif(STATE_VAL =='ST_VIET_14'):
        S_STATE_VAL = 14
            
    elif(STATE_VAL =='ST_VIET_15'):
        S_STATE_VAL = 15
            
    elif(STATE_VAL =='ST_VIET_16'):
        S_STATE_VAL = 16
        
    elif(STATE_VAL =='ST_VIET_17'):
        S_STATE_VAL = 17
            
    elif(STATE_VAL =='ST_VIET_18'):
        S_STATE_VAL = 18
            
    elif(STATE_VAL == 'ST_VIET_19'):
         S_STATE_VAL = 19
            
    elif(STATE_VAL =='ST_VIET_20'):
        S_STATE_VAL = 20
             
    elif(STATE_VAL =='ST_VIET_21'):
        S_STATE_VAL = 21
             
    elif(STATE_VAL =='ST_VIET_22'):
        S_STATE_VAL = 22
    elif(STATE_VAL =='ST_VIET_23'):
        S_STATE_VAL = 23
             
    elif(STATE_VAL =='ST_VIET_24'):
        S_STATE_VAL = 24
             
    elif(STATE_VAL =='ST_VIET_25'):
        S_STATE_VAL = 25
             
    elif(STATE_VAL =='ST_VIET_26'):
        S_STATE_VAL = 26
             
    elif(STATE_VAL =='ST_VIET_27'):
        S_STATE_VAL = 27
             
    elif(STATE_VAL =='ST_VIET_28'):
        S_STATE_VAL = 28
             
    elif(STATE_VAL =='ST_VIET_29'):
        S_STATE_VAL = 29
             
    elif(STATE_VAL =='ST_VIET_30'):
        S_STATE_VAL = 30
             
    elif(STATE_VAL =='ST_VIET_31'):
        S_STATE_VAL = 31
             
    elif(STATE_VAL =='ST_VIET_32'):
        S_STATE_VAL = 32
             
    elif(STATE_VAL =='ST_VIET_33'):
        S_STATE_VAL = 33
             
    elif(STATE_VAL =='ST_VIET_34'):
        S_STATE_VAL = 34
             
    elif(STATE_VAL =='ST_VIET_35'):
        S_STATE_VAL = 35
             
    elif(STATE_VAL =='ST_VIET_36'):
        S_STATE_VAL = 36
             
    elif(STATE_VAL =='ST_VIET_37'):
        S_STATE_VAL = 37
             
    elif(STATE_VAL =='ST_VIET_38'):
        S_STATE_VAL = 38
             
    elif(STATE_VAL =='ST_VIET_39'):
        S_STATE_VAL = 39
             
    elif(STATE_VAL =='ST_VIET_40'):
        S_STATE_VAL = 40
             
    elif(STATE_VAL =='ST_VIET_41'):
        S_STATE_VAL = 41
             
    elif(STATE_VAL =='ST_VIET_42'):
        S_STATE_VAL = 42
             
    elif(STATE_VAL =='ST_VIET_43'):
        S_STATE_VAL = 43
             
    elif(STATE_VAL =='ST_VIET_44'):
        S_STATE_VAL = 44
             
    elif(STATE_VAL =='ST_VIET_45'):
        S_STATE_VAL = 45
             
    elif(STATE_VAL =='ST_VIET_46'):
        S_STATE_VAL = 46
             
    elif(STATE_VAL =='ST_VIET_47'):
        S_STATE_VAL = 47
             
    elif(STATE_VAL =='ST_VIET_48'):
        S_STATE_VAL = 48
             
    elif(STATE_VAL =='ST_VIET_49'):
        S_STATE_VAL = 49
             
    elif(STATE_VAL =='ST_VIET_50'):
        S_STATE_VAL = 50
             
    elif(STATE_VAL =='ST_VIET_51'):
        S_STATE_VAL = 41
             
    elif(STATE_VAL =='ST_VIET_52'):
        
        S_STATE_VAL = 52
             
    elif(STATE_VAL =='ST_VIET_53'):
        S_STATE_VAL = 53
             
    elif(STATE_VAL =='ST_VIET_54'):
        S_STATE_VAL = 54
             
    elif(STATE_VAL =='ST_VIET_55'):
        S_STATE_VAL = 55
             
    elif(STATE_VAL =='ST_VIET_56'):
        S_STATE_VAL = 56
             
    elif(STATE_VAL =='ST_VIET_57'):
        S_STATE_VAL = 57
             
    elif(STATE_VAL =='ST_VIET_58'):
        S_STATE_VAL = 58
             
    elif(STATE_VAL == 'ST_VIET_59'):
        S_STATE_VAL = 59
             
    elif(STATE_VAL =='ST_VIET_60'):
        S_STATE_VAL = 60
             
    elif(STATE_VAL =='ST_VIET_61'):
        S_STATE_VAL = 61
             
    elif(STATE_VAL =='ST_VIET_62'):
        S_STATE_VAL = 62
             
    elif(STATE_VAL =='ST_VIET_63'):
        S_STATE_VAL = 63
             

            
    CLIENT_CD = request.form['CLIENT_CD']
    

    if CLIENT_CD == 'PA_CLNT_BAOVIET':
        
        S_CLIENT_CD = 0
    elif  CLIENT_CD =='PA_CLNT_DAIICHI':
        S_CLIENT_CD = 1
            
    elif CLIENT_CD == 'PA_CLNT_PVI':
        S_CLIENT_CD = 2
            
    elif CLIENT_CD == ' PA_CLNT_VBI':
        S_CLIENT_CD = 3

    TRNS_STATUS = request.form['PMNT_TRNS_STATUS']

    if TRNS_STATUS == 'PA_TRANS_STATUS_CP':
        S_TRANS_STATUS = 0
            
    elif TRNS_STATUS =='PA_TRANS_STATUS_FAIL':
        S_TRANS_STATUS = 1
            
    elif TRNS_STATUS == 'PA_TRANS_STATUS_PNDGP':
        S_TRANS_STATUS = 2
            
       
    TRANS_METHOD = request.form['TRANS_METHOD']
    
    
    if TRANS_METHOD == 'Bank':
        S_TRANS_METHOD = 0
            
    elif TRANS_METHOD == 'Online':
        S_TRANS_METHOD = 1
            
    elif TRANS_METHOD == 'PA_TRANS_BANK':
        S_TRANS_METHOD = 2
                
    elif TRANS_METHOD == 'PA_TRANS_FREE':
        S_TRANS_METHOD = 3
            
    elif TRANS_METHOD == 'PA_TRABS_ONLINE':
        S_TRANS_METHOD = 4
            
    elif TRANS_METHOD == 'PA_TRANS_PAT_AT_STORE':
        S_TRANS_METHOD = 5
            
    PRODUCT_CD = request.form['SUB_PRODUCT_CD']
    if(PRODUCT_CD == 'PAIN_HLT_CRTCILL'):
        S_SUB_PRODUCT_CD = 1
    elif(PRODUCT_CD == 'PAIN_LIFE'):
        S_SUB_PRODUCT_CD = 5
    elif(PRODUCT_CD == 'PAIN_NLIFE'):
        S_SUB_PRODUCT_CD = 6
    elif(PRODUCT_CD =='PAIN_HLT_HSPCSH'):
        S_SUB_PRODUCT_CD = 3
    elif(PRODUCT_CD == 'PAIN_HLT_HSPSRG'):
        S_SUB_PRODUCT_CD= 4
    elif(PRODUCT_CD == 'BaoVietLìfeCare'):
        S_SUB_PRODUCT_CD = 0
    else:
        S_SUB_PRODUCT_CD = 2
        
    data = [S_GENDER,S_SOURCE,S_LOCALE_VAL,S_STATE_VAL,S_CLIENT_CD,S_TRANS_METHOD,S_TRANS_STATUS,S_AMOUNT_I,S_AGE_I,S_SUB_PRODUCT_CD]
    print(data)
    column = ['GENDER', 'SOURCE', 'LOCALE_VAL', 'STATE_VAL', 'CLIENT_CD_x',
       'TRANS_METHOD', 'PMNT_TRNS_STATUS', 'AMOUNT_I','AGE_I','SUB_PRODUCT_CD']
    df = pd.DataFrame([data],columns = column)
    print(df)
    
    pred = model.predict(df)
    print(pred)
    op = ''
    flag = 0
    s = 0
    e = 0
    if(pred == 0):
        
        op = 'Active'
    else:
        flag = 1
        churn = joblib.load("ChurnDays.pkl")
        xPred = churn.predict(df)
        print(xPred)
        op = 'Churn'
        
        if(xPred == 0):
            s = 10
            e = 3359
        elif(xPred == 1):
            s = 3360
            e = 6687
        elif(xPred == 2):
            s = 6688
            e = 10014
        elif(xPred == 3):
            s = 10015
            e = 13342
        elif(xPred == 4):
            s = 13343
            e = 16670
        else:
            s = 16671
            e = 20000
    output = [op,s,e]
    #return jsonify({"The Category of user": op})
    return render_template('Random.html', prediction_text='{}'.format(output))
        
        
    


if __name__ == '__main__':
  
    model = joblib.load("RandomForest3.pkl") # Load "model.pkl"
    print ('Model loaded')
    app.run(port=9001, debug=True,use_reloader=False)
    