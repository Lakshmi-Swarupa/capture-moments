from flask import Flask,  render_template, request, jsonify

# step 1: Create the flask app instance
app = Flask(__name__)
#step 2: Dummy data for photographers(simulating database)
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "Sanju.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "Sanjana.jpg"},
    {"id": "p3", "name": "The Light Poets", "skills": ["Romantic", "Moody Aesthetic"], "image": "Couple.jpg"},
    {"id": "p4", "name": "Silversky Studio", "skills": ["Natural Light", "Cinematic"], "image": "Chinnu.jpg"}
]

availability_data = {
    "p1": ["2025-06-20","2025-06-23"],
    "p2": ["2025-06-19","2025-06-22"],
    "p3": ["2025-06-18","2025-06-21"],
    "p4": ["2025-06-17","2025-06-20"]
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/book', methods=['GET','POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        user_id = request.form.get('date')
        date = request.form.get('date')       
        return f"<h2 style='color:green'>Booking Confirmed! For {photographer_id} on {date}.</h2>"
    return render_template('book.html')

@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html',photographers=photographers,availability_data=availability_data)


if __name__ == '__main__':
    app.run(debug=True)