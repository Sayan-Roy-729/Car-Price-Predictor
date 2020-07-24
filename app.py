from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle


cars_dict = pickle.load(open('templates/Cars/All_cars.pkl', 'rb'))
companies = pickle.load(open('templates/Cars/cars_company(1).pkl', 'rb'))

# Cars of different companies 
Ambassador = pickle.load(open('templates/Cars/Ambassador.pkl', 'rb'))
Audi = pickle.load(open('templates/Cars/Audi.pkl', 'rb'))
Bentley = pickle.load(open('templates/Cars/Bentley.pkl', 'rb'))
Bmw = pickle.load(open('templates/Cars/BMW.pkl', 'rb'))
Chevrolet = pickle.load(open('templates/Cars/Chevrolet.pkl', 'rb'))
Datsun = pickle.load(open('templates/Cars/Datsun.pkl', 'rb'))
Fiat = pickle.load(open('templates/Cars/Fiat.pkl', 'rb'))
Force = pickle.load(open('templates/Cars/Force.pkl', 'rb'))
Ford = pickle.load(open('templates/Cars/Ford.pkl', 'rb'))
Honda = pickle.load(open('templates/Cars/Honda.pkl', 'rb'))
Hyundai = pickle.load(open('templates/Cars/Hyundai.pkl', 'rb'))
ISUZu = pickle.load(open('templates/Cars/ISUZU.pkl', 'rb'))
Isuzu = pickle.load(open('templates/Cars/Isuzu(1).pkl', 'rb'))
Jaguar = pickle.load(open('templates/Cars/Jaguar.pkl', 'rb'))
Jeep = pickle.load(open('templates/Cars/Jeep.pkl', 'rb'))
Lamborghini = pickle.load(open('templates/Cars/Lamborghini.pkl', 'rb'))
Land = pickle.load(open('templates/Cars/Land.pkl', 'rb'))
Mahindra = pickle.load(open('templates/Cars/Mahindra.pkl', 'rb'))
Maruti = pickle.load(open('templates/Cars/Maruti.pkl', 'rb'))
Mercedes_Benz = pickle.load(open('templates/Cars/Mercedes_Benz.pkl', 'rb'))
Mini = pickle.load(open('templates/Cars/Mini.pkl', 'rb'))
Mitsubishi = pickle.load(open('templates/Cars/Mitsubishi.pkl', 'rb'))
Nissan = pickle.load(open('templates/Cars/Nissan.pkl', 'rb'))
Porsche = pickle.load(open('templates/Cars/Porsche.pkl', 'rb'))
Renault = pickle.load(open('templates/Cars/Renault.pkl', 'rb'))
Skoda = pickle.load(open('templates/Cars/Skoda.pkl', 'rb'))
Smart = pickle.load(open('templates/Cars/Smart.pkl', 'rb'))
Tata = pickle.load(open('templates/Cars/Tata.pkl', 'rb'))
Toyota = pickle.load(open('templates/Cars/Toyota.pkl', 'rb'))
Volkswagen = pickle.load(open('templates/Cars/Volkswagen.pkl', 'rb'))
Volvo = pickle.load(open('templates/Cars/Volvo.pkl', 'rb'))



# print(companies['Maruti'])


app = Flask(__name__)


@app.route('/')
def hello_world(companies = companies):
    return render_template('car_company.html', companies = companies)


@app.route('/car_companies', methods = ['POST'])

def car_companies(Maruti = Maruti, Hyundai = Hyundai, Honda = Honda, Toyota = Toyota, Mercedes_Benz = Mercedes_Benz, Volkswagen = Volkswagen, Ford = Ford, Mahindra = Mahindra, Bmw = Bmw, Audi = Audi, Tata = Tata, Skoda = Skoda, Renault = Renault, Chevrolet = Chevrolet, Nissan = Nissan, Land =  Land, Jaguar = Jaguar, Mitsubishi = Mitsubishi, Mini = Mini, Fiat = Fiat, Volvo = Volvo, Porsche = Porsche, Jeep = Jeep, Datsun = Datsun, Force = Force,  ISUZu = ISUZu, Smart = Smart, Isuzu = Isuzu, Lamborghini = Lamborghini, Ambassador = Ambassador, Bentley = Bentley):


    company_name  = request.form.get("car_company")

    if company_name == 'Maruti':
        company_number = companies['Maruti']
        car_numbers = len(Maruti)
        car_name = Maruti
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Hyundai':
        company_number = companies['Hyundai']
        car_numbers = len(Hyundai)
        car_name = Hyundai
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number) 

    elif company_name == 'Honda':
        company_number = companies['Honda']
        car_numbers = len(Honda)
        car_name = Honda
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Toyota':
        company_number = companies['Toyota']
        car_numbers = len(Toyota)
        car_name = Toyota
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Mercedes-Benz':
        company_number = companies['Mercedes-Benz']
        car_numbers = len(Mercedes_Benz)
        car_name = Mercedes_Benz
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Volkswagen':
        company_number = companies['Volkswagen']
        car_numbers = len(Volkswagen)
        car_name = Volkswagen
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Ford':
        company_number = companies['Ford']
        car_numbers = len(Ford)
        car_name = Ford
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Mahindra':
        company_number = companies['Mahindra']
        car_numbers = len(Mahindra)
        car_name = Mahindra
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'BMW':
        company_number = companies['BMW']
        car_numbers = len(Bmw)
        car_name = Bmw
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Audi':
        company_number = companies['Audi']
        car_numbers = len(Audi)
        car_name = Audi
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Tata':
        company_number = companies['Tata']
        car_numbers = len(Tata)
        car_name = Tata
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Skoda':
        company_number = companies['Skoda']
        car_numbers = len(Skoda)
        car_name = Skoda
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Renault':
        company_number = companies['Renault']
        car_numbers = len(Renault)
        car_name = Renault
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Chevrolet':
        company_number = companies['Chevrolet']
        car_numbers = len(Chevrolet)
        car_name = Chevrolet
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Nissan':
        company_number = companies['Nissan']
        car_numbers = len(Nissan)
        car_name = Nissan
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Land':
        company_number = companies['Land']
        car_numbers = len(Land)
        car_name = Land
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Jaguar':
        company_number = companies['Jaguar']
        car_numbers = len(Jaguar)
        car_name = Jaguar
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Mitsubishi':
        company_number = companies['Mitsubishi']
        car_numbers = len(Mitsubishi)
        car_name = Mitsubishi
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Mini':
        company_number = companies['Mini']
        car_numbers = len(Mini)
        car_name = Mini
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Fiat':
        company_number = companies['Fiat']
        car_numbers = len(Fiat)
        car_name = Fiat
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Volvo':
        company_number = companies['Volvo']
        car_numbers = len(Volvo)
        car_name = Volvo
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Porsche':
        company_number = companies['Porsche']
        car_numbers = len(Porsche)
        car_name = Porsche
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Jeep':
        company_number = companies['Jeep']
        car_numbers = len(Jeep)
        car_name = Jeep
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Datsun':
        company_number = companies['Datsun']
        car_numbers = len(Datsun)
        car_name = Datsun
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Force':
        company_number = companies['Force']
        car_numbers = len(Force)
        car_name = Force
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'ISUZU':
        company_number = companies['ISUZU']
        car_numbers = len(ISUZu)
        car_name = ISUZu
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Smart':
        company_number = companies['Smart']
        car_numbers = len(Smart)
        car_name = Smart
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Isuzu':
        company_number = companies['Isuzu']
        car_numbers = len(Isuzu)
        car_name = Isuzu
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Lamborghini':
        company_number = companies['Lamborghini']
        car_numbers = len(Lamborghini)
        car_name = Lamborghini
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Ambassador':
        company_number = companies['Ambassador']
        car_numbers = len(Ambassador)
        car_name = Ambassador
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)

    elif company_name == 'Bentley':
        company_number = companies['Bentley']
        car_numbers = len(Bentley)
        car_name = Bentley
        return render_template('car_name.html', car_name = car_name, car_numbers = car_numbers, company_number = company_number)



@app.route('/car_names', methods = ['POST'])
def car_names():
    
    car_name  = request.form.get("car_name")
    # print(car_name)

    if car_name in Maruti:
        company_number = companies['Maruti']

    elif car_name in Hyundai:
        company_number = companies['Hyundai']

    elif car_name in Honda:
        company_number = companies['Honda']

    elif car_name in Toyota:
        company_number = companies['Toyota']

    elif car_name in Mercedes_Benz:
        company_number = companies['Mercedes-Benz']

    elif car_name in Volkswagen:
        company_number = companies['Volkswagen']

    elif car_name in Ford:
        company_number = companies['Ford']

    elif car_name in Mahindra:
        company_number = companies['Mahindra']

    elif car_name in Bmw:
        company_number = companies['BMW']

    elif car_name in Audi:
        company_number = companies['Audi']

    elif car_name in Tata:
        company_number = companies['Tata']

    elif car_name in Skoda:
        company_number = companies['Skoda']

    elif car_name in Renault:
        company_number = companies['Renault']

    elif car_name in Chevrolet:
        company_number = companies['Chevrolet']

    elif car_name in Nissan:
        company_number = companies['Nissan']

    elif car_name in Land:
        company_number = companies['Land']

    elif car_name in Jaguar:
        company_number = companies['Jaguar']

    elif car_name in Mitsubishi:
        company_number = companies['Mitsubishi']

    elif car_name in Mini:
        company_number = companies['Mini']

    elif car_name in Fiat:
        company_number = companies['Fiat']

    elif car_name in Volvo:
        company_number = companies['Volvo']

    elif car_name in Porsche:
        company_number = companies['Porsche']

    elif car_name in Jeep:
        company_number = companies['Jeep']

    elif car_name in Datsun:
        company_number = companies['Datsun']

    elif car_name in Force:
        company_number = companies['Force']

    elif car_name in ISUZu:
        company_number = companies['ISUZU']

    elif car_name in Smart:
        company_number = companies['Smart']

    elif car_name in Isuzu:
        company_number = companies['Isuzu']

    elif car_name in Lamborghini:
        company_number = companies['Lamborghini']

    elif car_name in Ambassador:
        company_number = companies['Ambassador']

    elif car_name in Bentley:
        company_number = companies['Bentley']

    # print(company_number)



    
    car_number = cars_dict[f"{car_name}"]
    # print(car_number)


    # # print(company_number)

    # # features -------> 
    year  = request.form.get("year")
    # print(f"The value of year is {year}")

    km_driven  = request.form.get("km_driven")
    # print(f"The value of km_driven is {km_driven}")

    fuel_type  = request.form.get("fuel_type")
    # print(f"The value of fuel_type is {fuel_type}")


    engine_power  = request.form.get("engine_power")
    # print(f"The value of engine_power is {engine_power}")
    # # company_number
    # # car_number 
    

    # # trained model ----->
    regressor = pickle.load(open('templates/Cars/car_prediction_model.pkl', 'rb'))

    # # predict the price ------>
    predicted_price = regressor.predict([[year, km_driven, fuel_type, engine_power, company_number, car_number ]])[0] 

    return render_template('result.html', predicted_price = int(predicted_price))

if __name__ == '__main__':
    app.run(debug=True)
