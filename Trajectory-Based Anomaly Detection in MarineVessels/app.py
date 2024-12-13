from flask import Flask, render_template, request, redirect,session 
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load pre-trained models and preprocessing objects
with open('svr_model.pkl', 'rb') as f:
    svr_model = pickle.load(f)
with open('logreg_model.pkl', 'rb') as f:
    logreg_model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('pca.pkl', 'rb') as f:
    pca = pickle.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, subject, email, phone, message):
        self.name = name
        self.subject = subject
        self.email = email
        self.phone = phone
        self.message = message

with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/svr')
def svr():
    return render_template('svr.html')

@app.route('/logistic')
def logistic():
    return render_template('logistic.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        email = request.form['email']
        phone = request.form['number']
        message = request.form['message']

        new_contact = Contact(name=name, subject=subject, email=email, phone=phone, message=message)
        db.session.add(new_contact)
        db.session.commit()
        return redirect('/contact')  # Redirect to the same page or a thank-you page

    return render_template('contact.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract input data from form
        try:
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            sog = float(request.form['sog'])
            cog = float(request.form['cog'])
            heading = float(request.form['heading'])
            length = float(request.form['length'])
            width = float(request.form['width'])
            draft = float(request.form['draft'])
            cargo = float(request.form['cargo'])
            speed_delta = float(request.form['speed_delta'])
            course_delta = float(request.form['course_delta'])
        except ValueError:
            return "Invalid input data. Please check your inputs."

        # Combine features into a single numpy array
        features = np.array([[lat, lon, sog, cog, heading, length, width, draft, cargo, speed_delta, course_delta]])

        # Standardize the input data
        scaled_features = scaler.transform(features)

        # Apply PCA for dimensionality reduction
        pca_features = pca.transform(scaled_features)

        # Choose the prediction model based on user selection
        model_choice = request.form['model_choice']

        if model_choice == 'svr':
            # SVR Model Prediction (Regressor)
            svr_prediction = svr_model.predict(pca_features)

            # Define a threshold for classifying as anomalous or not
            threshold = 1.0
            is_anomalous = abs(svr_prediction[0]) > threshold
            prediction = "Anomalous" if is_anomalous else "Normal"

        elif model_choice == 'logreg':
            # Logistic Regression Prediction (Classifier)
            logreg_prediction = logreg_model.predict(pca_features)
            prediction = "Anomalous" if logreg_prediction[0] == 1 else "Normal"

        else:
            return "Invalid model choice."

        # Render the result
        return render_template('predictor.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
