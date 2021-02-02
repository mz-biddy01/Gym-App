import datetime
import pdb
from models.session import Session
from models.member import Member
from models.booking import Booking

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

memeber1 = Member('Jason', 'Smith')
member_repository.save(memeber1)

memeber2 = Member('Johnny', 'Bravo')
member_repository.save(memeber2)

member3 = Member('Bart', 'Simpson')
member_repository.save(member3)

member4 = Member('Craig', 'Gough')
member_repository.save(member4)

member5 = Member('Ally', 'McGilloway')
member_repository.save(member5)

member6 = Member('Wendy', 'Williams')
member_repository.save(member6)

session1 = Session('Yoga', 'Steve')
session_repository.save(session1)

session2 = Session('Swimming', 'Allison')
session_repository.save(session2)

session3 = Session('Cycling', 'Helena')
session_repository.save(session3)

session4 = Session('Body_building', 'Scott')
session_repository.save(session4)

booking1 = Booking(datetime.date(2020, 3, 4), 1, 1)
booking_repository.save(booking1)

booking2 = Booking(datetime.date(2020, 3, 6), 3, 4)
booking_repository.save(booking2)

booking3 = Booking(datetime.date(2020, 5, 19), 4, 2)
booking_repository.save(booking3)

booking4 = Booking(datetime.date(2020, 5, 27), 2, 3)
booking_repository.save(booking4)

booking5 = Booking(datetime.date(2020, 6, 1), 1, 5)
booking_repository.save(booking5)

booking6 = Booking(datetime.date(2020, 6, 9), 4, 6)
booking_repository.save(booking6)

booking7 = Booking(datetime.date(2020, 3, 4), 1, 2)
booking_repository.save(booking7)

booking8 = Booking(datetime.date(2020, 3, 4), 1, 3)
booking_repository.save(booking8)

booking9 = Booking(datetime.date(2020, 3, 6), 3, 5)
booking_repository.save(booking9)

booking10 = Booking(datetime.date(2020, 3, 6), 3, 4)
booking_repository.save(booking10)

booking11 = Booking(datetime.date(2020, 5, 19), 4, 6)
booking_repository.save(booking11)

booking12 = Booking(datetime.date(2020, 5, 19), 4, 5)
booking_repository.save(booking12)

booking13 = Booking(datetime.date(2020, 5, 27), 2, 1)
booking_repository.save(booking13)

booking14 = Booking(datetime.date(2020, 5, 27), 2, 6)
booking_repository.save(booking14)

booking15 = Booking(datetime.date(2020, 6, 1), 1, 2)
booking_repository.save(booking15)

booking16 = Booking(datetime.date(2020, 6, 1), 1, 1)
booking_repository.save(booking16)

booking17 = Booking(datetime.date(2020, 6, 9), 4, 5)
booking_repository.save(booking17)

booking18 = Booking(datetime.date(2020, 6, 9), 4, 3)
booking_repository.save(booking18)






pdb.set_trace()