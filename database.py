import psycopg2

connection = psycopg2.connect(host='kesavan.db.elephantsql.com', dbname='rwwdjumw', user='rwwdjumw',
                              password='Ndg6c_RJc7868a4HcK3WJinVRWqL4RTr')

cursor = connection.cursor()


def add_item(name, link, img):
    cursor.execute('insert into items(product, link, img) values(%s, %s, %s)', [name, link, img])


def commit():
    connection.commit()
