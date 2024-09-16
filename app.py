from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    company = request.form.get('company')
    photo = request.files.get('photo')

    # Print data to the console
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Company: {company}")

    # If a photo was uploaded
    if photo:
        photo.save(f"./uploads/{photo.filename}")  # Save file to an 'uploads' directory

    return jsonify({"status": "success", "message": "Data received successfully."})

if __name__ == "__main__":
    app.run(debug=True)
