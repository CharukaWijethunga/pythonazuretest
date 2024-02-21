from flask import Flask, render_template, request
import xlsxwriter
app = Flask(__name__)

@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run()