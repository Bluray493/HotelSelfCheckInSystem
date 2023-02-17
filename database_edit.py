import sqlite3
from sqlite3 import Error
from _sqlite3 import INSERT


def create_connection(db_file):
    """create a database connection to the SQLite database
     specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


sql_create_reservation_table = """ CREATE TABLE IF NOT EXISTS reservations (
reservation_id integer PRIMARY KEY,
room_id integer,
check_in_date text,
check_out_date text,
FOREIGNKEY(reservation_id)REFERENCES users (user_id)
FOREIGN KEY (room_id) REFERENCES rooms (room_id)
); """


sql_create_user_table = """CREATE TABLE IF NOT EXISTS users (
user_id PRIMARY KEY,
name text NOT NULL,
email text,
phone_number text,);"""


sql_create_rooms_table = """CREATE TABLE IF NOT EXISTS rooms (
room_id PRIMARY KEY,
room_type NOT NULL,
floor INT
);"""

INSERT into
reservations(reservation_id, room_id, check_in_date, check_out_date)

VALUES
(12344, 2234, dd/mm/yyyy, dd/mm/yyyy),
(12344, 2234, dd/mm/yyyy, dd/mm/yyyy),
(12344, 2234, dd/mm/yyyy, dd/mm/yyyy)

INSERT into
rooms(room_id, room_type, floor)

VALUES
(12344, single, 2),
(12344, double, 3),
(12344, appartment, , 23),
(12344, luxury, 43)


Insert into
users(user_id, name, email, phone_number)

VALUES
(12344, John, jh67@gmail.com, +4478965233),
(12344, John, jh67@gmail.com, +4478965233),
(12344, John, jh67@gmail.com, +4478965233),
(12344, John, jh67@gmail.com, +4478965233)


def main():
    # create a database connection
    conn = sqlite3.connect("tutorial.db")

    # create tables
    if conn is not None:
        # create user table
        create_table(conn, sql_create_user_table)

        # create reservationn tables
        create_table(conn, sql_create_reservation_table)

        # create room table
        create_table(conn, sql_create_rooms_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    main()
