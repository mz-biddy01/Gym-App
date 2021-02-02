from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from project_work.models.session import Session
import project_work.repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/show_sessions.html", sessions = sessions)


@sessions_blueprint.route("/show_new_session_form", methods=['GET', 'POST'])
def show_new_session_form():
    if request.method == 'POST':
        name = request.form['name']
        instructor_name = request.form['instructor']
        newsession = Session(name=name.title(), instructor_name=instructor_name.title())
        session_repository.save(newsession)
        return redirect(url_for('sessions.sessions'))
    return render_template("sessions/add_session.html")


@sessions_blueprint.route("/edit_session", methods=['POST'])
def edit_session():
    session_name = request.form['new_name']
    instructor_name = request.form['new_instructor']
    session_id = request.form['session_id']
    updated_session = Session(session_name.title(), instructor_name.title(), int(session_id))
    session_repository.update(updated_session)
    return redirect(url_for('sessions.sessions'))


@sessions_blueprint.route("/view_session_booking", methods=['POST', 'GET'])
def view_session_booking():
    sessions = session_repository.select_all()
    if request.method == 'POST':
        session_name = request.form['sessions']
        session_id = int(session_name.split(' - ')[0])
        session_name = session_name.split(' - ')[1]
        instructor_name = session_name.split(' - ')[-1]
        session = Session(session_name, instructor_name, session_id)
        members = session_repository.members(session)
        return render_template("sessions/view_session_booking.html", sessions = sessions, members = members)
        # return redirect(url_for('sessions.view_session_booking', members=members))
    
    return render_template("sessions/view_session_booking.html", sessions = sessions)
