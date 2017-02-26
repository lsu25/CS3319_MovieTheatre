from movie_Theatre import app
from flask import Flask, render_template, request, session
import mysql.connector

@app.route('/listcustomers')
def listCustomers():
    listCustomers="true"
    deleteCustomer="false"
    editCustomer="false"
    addCustomer="false"
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = (
        "SELECT idCustomer, FirstName, LastName, EmailAddress, CAST(Sex AS CHAR CHARACTER SET utf8) AS Sex FROM Customer ORDER BY LastName")
		
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    return render_template('customer.html',ListCustomers=listCustomers, DeleteCustomer=deleteCustomer, EditCustomer=editCustomer,AddCustomer=addCustomer, customers=customers)
	
@app.route('/addcustomer')
def addCustomer():
    listCustomers="false"
    deleteCustomer="false"
    editCustomer="false"
    addCustomer="true"
    return render_template('customer.html',ListCustomers=listCustomers, DeleteCustomer=deleteCustomer, EditCustomer=editCustomer,AddCustomer=addCustomer)

@app.route('/submitcustomer', methods=["POST"])
def submitCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Customer (FirstName, LastName, EmailAddress, Sex) "
        "VALUES (%s, %s, %s, %s)"
    )
    data = (request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
    cursor.execute(insert_stmt, data)
    cnx.commit()
    cnx.close()
	
    return addCustomer()
	
@app.route('/deletecustomer')
def deleteCustomer():
    listCustomers="false"
    deleteCustomer="true"
    editCustomer="false"
    addCustomer="false"
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT idCustomer, FirstName, LastName, EmailAddress, CAST(Sex AS CHAR CHARACTER SET utf8) AS Sex  FROM Customer ORDER BY LastName")
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
	
    return render_template('customer.html',ListCustomers=listCustomers, DeleteCustomer=deleteCustomer, EditCustomer=editCustomer,AddCustomer=addCustomer, customers=customers)

@app.route('/removecustomer', methods=["POST"])
def removeCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
	
    idCustomer = request.form['idCustomer']
	
    delete_attend = ("DELETE FROM Attend WHERE Customer_idCustomer = '" + idCustomer +"'")
    cursor.execute(delete_attend, idCustomer)
	
    delete_customer = (
    "DELETE FROM Customer WHERE FirstName = %s AND LastName = %s AND EmailAddress = %s ")
    data = (request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'])
    cursor.execute(delete_customer, data)
    cnx.commit()
    cnx.close()
	
    return deleteCustomer()
	
@app.route("/editcustomer")
def editCustomer():
    listCustomers="false"
    deleteCustomer="false"
    editCustomer="true"
    addCustomer="false"
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT idCustomer, FirstName, LastName, EmailAddress, CAST(Sex AS CHAR CHARACTER SET utf8) AS Sex FROM Customer" )
    cursor.execute(query)
    customers=cursor.fetchall()
    cnx.close()
    
    return render_template('customer.html',ListCustomers=listCustomers, DeleteCustomer=deleteCustomer, EditCustomer=editCustomer,AddCustomer=addCustomer, customers=customers)

@app.route("/updatecustomer", methods=["POST"])	
def updateCustomer():
    idCustomer = request.form['idCustomer']
    
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    update_stmt = (
        "UPDATE Customer SET FirstName = %s, LastName = %s, EmailAddress = %s, Sex = %s WHERE idCustomer = " + str(idCustomer) + "")
    data = (request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
    print("Attempting: " + update_stmt)
    cursor.execute(update_stmt, data)
    cnx.commit()
    cnx.close()
	
    return editCustomer()