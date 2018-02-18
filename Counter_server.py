from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'TheSecretKey'

# counter tracks the count on the server-side
counter = 0

@app.route('/')
def index():
    global counter
    counter += 1
    return render_template('index.html', count = counter)

@app.route('/twoTick', methods=['POST'])
def twoTick():
    global counter
    counter +=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resets():
    global counter
    counter = -1
    return redirect('/')

app.run(debug=True)