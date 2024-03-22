from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello_home():
    return '<p> You have reached home page </p> <img src="https://www.nokia.com/sites/default/files/styles/scale_720_not_convert_webp/public/2023-02/nokia-refreshed-logo-1_1.jpg" />'

app.run(host="0.0.0.0", port=5000)
