from project_work.db.run_sql import run_sql

from project_work.models.booking import Booking
from project_work.models.member import Member
import project_work.repositories.session_repository as session_repository
import project_work.repositories.member_repository as member_repository


def save(booking):
    sql = "INSERT INTO bookings(date, session_id, member_id) VALUES (%s, %s, %s) RETURNING id"
    values =[booking.date, booking.session_id, booking.member_id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        session = session_repository.select(row['session_id'])
        full_name = f"{member.first_name} {member.last_name}"
        booking = Booking(row['date'], session.name, full_name, row['id'])
        bookings.append(booking)
    return bookings


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
