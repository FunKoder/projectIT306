from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/Menu')
def menu():
    return render_template('menu.html')

@app.route('/Transaction')
def transact():
    return render_template('transaction.html')

@app.route('/Order')
def order():
    return render_template('order.html')

@app.route('/Thankyou')
def thx():
    return render_template('thank.html')

if __name__ == '__main__':
    app.run()
