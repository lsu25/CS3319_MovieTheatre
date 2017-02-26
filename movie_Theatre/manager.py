from movie_Theatre import app
from flask import Flask, render_template, request, session
import mysql.connector

@app.route('/manager')
def manager():
    return render_template('manager.html')
	
@app.route('/attendance')
def attendance():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    query = (
        "SELECT Attend.*, Customer.FirstName, Customer.LastName, Showing.ShowingDateTime, "
		"Movie.idMovie, Movie.MovieName FROM Attend JOIN Customer ON Attend.Customer_idCustomer = "
		"Customer.idCustomer JOIN Showing ON Attend.Showing_idShowing = Showing.idShowing JOIN Movie ON "
		"Showing.Movie_idMovie = Movie.idMovie")
    cursor.execute(query)
    attendance=cursor.fetchall()
    cnx.close()
    return render_template('attendance.html', attendance=attendance)
	
@app.route("/managermenu", methods=["POST"])	
def returnManager():
    return render_template('manager.html')	
    