def create_table(con, cur, path):
    cur.execute(path)
    con.commit()