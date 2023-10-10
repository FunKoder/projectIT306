from flask import Flask, redirect, url_for, request, render_template
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbfood'
)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/Menu')
def menu():
    return render_template('menu.html')

@app.route('/getorder', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        food = request.form.get('food')
        if food == "Cheese Burger":
            a = 45
        else:
            a = 35

        drink = request.form.get('drink')
        if drink == "Tasty Water":
            b = 5
        else:
            b = 25

        dessert = request.form.get('dessert')
        if dessert == "Almond sundae":
            c = 38
        else:
            c = 32

        amount = int(request.form.get('amount'))
        price = (a + b + c) * amount

        mycursor = conn.cursor()
        sql = "INSERT INTO foodtable (food,drink,dessert,price,amount) VALUES (%s,%s,%s,%s,%s)"
        data = (food, drink, dessert, price, amount)
        mycursor.execute(sql, data)
        conn.commit()
        mycursor1 = conn.cursor()
        sql = "SELECT * FROM foodtable"
        mycursor1.execute(sql)
        myresult = mycursor1.fetchall()
        if myresult:
            return render_template('order.html', order=myresult)

@app.route('/Order', methods=['POST', 'GET'])
def order():
        mycursor = conn.cursor()
        sql = "SELECT * FROM foodtable"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult:
            return render_template('order.html', order=myresult)

@app.route('/edit/<orderid>', methods=['POST', 'GET'])
def edit(orderid):
    if request.method == 'GET':
        mycursor = conn.cursor()
        sql = "SELECT * FROM foodtable WHERE orderid=%s"
        data = (orderid,)
        mycursor.execute(sql, data)
        myresult = mycursor.fetchall()
        if myresult:
            return render_template('updateorder.html', myresult=myresult)

@app.route('/editorder', methods=['POST', 'GET'])
def editorder():
    if request.method == 'POST':
        orderid = request.form['orderid']
        food = request.form.get('food')
        if food == "Cheese Burger":
            a = 45
        else:
            a = 35

        drink = request.form.get('drink')
        if drink == "Tasty Water":
            b = 5
        else:
            b = 25

        dessert = request.form.get('dessert')
        if dessert == "Almond sundae":
            c = 38
        else:
            c = 32

        amount = int(request.form.get('amount'))
        price = (a + b + c) * amount

        mycursor = conn.cursor()
        sql = "UPDATE foodtable SET food=%s,drink=%s,dessert=%s,price=%s,amount =%s WHERE orderid=%s"
        data = (food, drink, dessert, price,amount, orderid)
        mycursor.execute(sql, data)
        conn.commit()
        mycursor1 = conn.cursor()
        sql = "SELECT * FROM foodtable"
        mycursor1.execute(sql)
        myresult = mycursor1.fetchall()
        if myresult:
            return render_template('order.html', order=myresult)

@app.route('/deleteorder/<orderid>')
def deleteorder(orderid):
    mycursor = conn.cursor()
    sql = "DELETE FROM foodtable WHERE orderid=%s"
    data = (orderid,)
    mycursor.execute(sql, data)
    conn.commit()
    mycursor1 = conn.cursor()
    sql = "SELECT * FROM foodtable"
    mycursor1.execute(sql)
    myresult = mycursor1.fetchall()
    if myresult:
        return render_template('order.html', order=myresult)
    else:
        return render_template('order.html')

@app.route('/Thankyou')
def thx():
    return render_template('thank.html')

if __name__ == '__main__':
    app.run(debug=True)
