from project_work.db.run_sql import run_sql

from project_work.models.session import Session
from project_work.models.member import Member


def save(session):
    sql = "INSERT INTO sessions(name, instructor_name) VALUES (%s, %s) RETURNING id"
    values = [session.name, session.instructor_name]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['instructor_name'], row['id'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0] 

    if result is not None:
        session = Session(result['name'], result['instructor_name'])
    return session

def update(session):
    sql = "UPDATE sessions SET name = %s, instructor_name = %s WHERE id = %s"
    values = [session.name, session.instructor_name, session.id]
    run_sql(sql, values)

def members(session):
    members = []

    sql = "SELECT DISTINCT members.* From members INNER JOIN bookings ON bookings.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'])
        members.append(member)

    return members