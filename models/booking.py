class Booking:
    def __init__(self, date, session_id, member_id, id = None):
        self.date = date
        self.session_id = session_id
        self.member_id = member_id
        self.id = id