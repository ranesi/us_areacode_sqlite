import sqlite3

"""
Was created using the CSV file found at:
<https://github.com/ravisorg/Area-Code-Geolocation-Database>
So special thanks to 'ravisorg'
"""

sqlf = [
    'init_db.sql',
    'define_db.sql',
    'insert_into.sql',
]
ac_file = 'us-area-code-cities.csv'


def read_file(filename):
    with open(filename, 'r') as f:
        ret = f.read()
    return ret


def parse_usa_codes():
    ret = []
    f = read_file(ac_file)
    l = f.split('\n')
    for row in l:
        x = row.split(',')
        ret.append(x)
    print(ret)
    return ret


def create_db():
    """Defines the US Area Code Database"""
    init = read_file(sqlf[0])
    schema = read_file(sqlf[1])

    conn = sqlite3.connect('us_areacodes.db')
    cur = conn.cursor()

    cur.execute(init)
    cur.execute(schema)

    conn.commit()
    conn.close()


def populate_db(data):

    insert = read_file(sqlf[2])

    conn = sqlite3.connect('us_areacodes.db')
    cur = conn.cursor()

    for x in data:
        # 0 - areacode, 1 - city, 2 - state,
        # 3 - country, 4 - latitude, 5 - longitude
        if len(x) < 6:
            continue
        else:
            cur.execute(insert, (x[0], x[1], x[2], x[3], x[4], x[5]))

    conn.commit()
    conn.close()


def main():

    data = parse_usa_codes()

    create_db()
    populate_db(data)


if __name__ == '__main__':
    main()
