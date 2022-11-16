from flask import Flask , request , jsonify
from flask_cors import CORS



import util

app = Flask(__name__)
CORS(app)

@app.route('/greeting')

def greeting():
    return 'Happy Rakshabandhan Rajan'

@app.route('/get_pool', methods=['GET','POST'])
def get_pool():
    response = jsonify({
        'pool': util.get_pool()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response

@app.route('/get_program_duration', methods=['GET','POST'])
def get_program_duration():
    response = jsonify({
        'program_duration': util.get_program_duration()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response

@app.route('/degree_name', methods=['GET','POST'])
def get_degree_name():
    response = jsonify({
        'degree_name': util.get_degree_name()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response

@app.route('/get_category', methods=['GET','POST'])
def get_category():
    response = jsonify({
        'category': util.get_category()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response


@app.route('/get_instituteName', methods=['GET','POST'])
def get_instituteName():
    response = jsonify({
        'institute_name': util.get_instituteName()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response

@app.route('/get_department_name', methods=['GET','POST'])
def get_department_name():
    response = jsonify({
        'department': util.get_department_name()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response


@app.route('/predictCrank' , methods=['POST'])
def predictCrank():
    year = float(request.form['year'])
    pool = request.form['pool']
    program_duration = request.form['program_duration']
    degree = request.form['degree_name']
    category = request.form['category']
    institute = request.form['institute_name']
    department = request.form['department']

    response = jsonify({
        'predictedCrank': util.get_predictedCrank(year,pool,program_duration,degree,category,institute,department )
    })

    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For IIT Closing Rank Prediction...")
    app.run()