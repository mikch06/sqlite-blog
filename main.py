import sqlite3
con = sqlite3.connect("data/blog.db")

cur = con.cursor()

# cur.execute("create table picblog(date, title, comment, image)")

cur.execute("""
    insert into picblog values
        ('2024.04.18', 'Chateaux Meyney', 'best', 'IMG_4058.jpg')
""")


con.commit()