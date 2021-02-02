DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    instructor_name VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    session_id SERIAL REFERENCES sessions(id) ON DELETE CASCADE,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE
);