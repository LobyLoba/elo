from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def homepage():
    return render_template('/index.html')

# Route for the happy birthday page
@app.route('/happy_birthday')
def happy_birthday():
    return render_template('happy_birthday.html')

# Route for the blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)