#!python

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def bmi():
    
    if request.method=="POST" and 'weight' in request.form:
        weight=float(request.form.get('weight'))
        height=float(request.form.get('height'))
        bmi=round((weight/((height/100)**2)),2)
        return render_template("bmipage.html",bmi=bmi)
    """bmi= calc_bmi(weight,height)"""
    
    elif request.method=="POST" and !('weight') or !('height') in request.form:
        return render_template("bmipage.html",bmi="Enter all the details")
    
    
"""def calc_bmi(weight,height):
    return round((weight/((height/100)**2)),2)"""
    
app.run()