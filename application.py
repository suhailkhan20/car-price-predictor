from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

car = pd.read_csv('Cleaned Car.csv')

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years =  sorted(car['year'].unique())
    fuel_types =  sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models , years=years, fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('type')
    kilo_driven = int(request.form.get('kilo_driven'))

    # Dummy logic for now — replace with your ML model prediction
    predicted_price = 500000 - (2025 - year) * 10000 - kilo_driven * 0.5

    return str(int(predicted_price))

if __name__ == "__main__":
    app.run(debug=True)