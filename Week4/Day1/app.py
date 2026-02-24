from flask import Flask

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to Flask Backend Project!</h1>"

# Run server
if __name__ == '__main__':
    app.run(debug=True)