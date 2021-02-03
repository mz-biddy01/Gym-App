from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from project_work.repositories import booking_repository
from project_work.repositories import member_repository
from project_work.repositories import session_repository
from project_work.models.booking import Booking


bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/list.html", bookings = bookings)

@bookings_blueprint.route("/bookings/<id>")
def show(id):
    booking = booking_repository.select(id)
    render_template("bookings/list.html", booking = booking)


@bookings_blueprint.route("/make_booking", methods=['POST', 'GET'])
def make_booking():
    if request.method == 'POST':
        session_name = request.form['sessions']
        session_id = int(session_name.split(' - ')[0])
        
        member_name = request.form['members']
        member_id = int(member_name.split(' - ')[0])
        session_date = request.form['session-date']
        booking = Booking(session_date, session_id, member_id)
        booking_repository.save(booking)
        return redirect(url_for('bookings.make_booking'))
        
    sessions = session_repository.select_all()
    members = member_repository.select_all()
    return render_template("bookings/make_booking.html", sessions = sessions, members = members)


@bookings_blueprint.route("/delete_booking", methods=['POST'])
def delete_booking():
    booking_id = request.form['booking_id']
    booking_id = int(booking_id)
    booking_repository.delete(booking_id)
    return redirect(url_for('bookings.bookings'))