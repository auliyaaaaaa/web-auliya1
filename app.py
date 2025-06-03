from flask import flask , render_template , request
app = flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/attendance', methods=['GET', 'POS'])

@app.route('/')
def attendance():
    if request.method == 'POST':
        # Handle attendance submission
        name = request.form.get('name')
        #proccess the attendance data here
        
    return render_template('success.html' , name=name)

    return render_template('attendance.html')

from flask import Flask, render_template, request

 
