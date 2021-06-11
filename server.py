import random
from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)

app.secret_key='this is the secret key'

@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number']=random.randint(1, 100)
        session['guess_num']=0
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    print(request.form)
    session['guess_num']+=1
    session['guess']=int(request.form['guess'])
    if session['guess']==session['random_number']:
        session['guess']='correct'
    elif session['guess_num']<5:
        if session['guess']>session['random_number']:
            session['guess']='high'
        elif session['guess']<session['random_number']:
            session['guess']='low'
    else:
        session['guess']='loss'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)