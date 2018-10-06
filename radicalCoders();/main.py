from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register/')
def home2():
    return render_template('register.html')

@app.route('/home/')
def home3():
    return render_template('defaultview.html')

@app.route('/admin/')
def home4():
    return render_template('admin.html')

@app.route('/zoning_code/')
def home5():
    return render_template('zoning_codes.html')

@app.route('/donate/')
def home6():
    return render_template('donation.html')

if __name__ == '__main__':
    app.run(debug=True)
