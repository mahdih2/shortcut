
from shortcut.app.models import Post
from shortcut.db.generate_path import generate_path
from shortcut.db.create_db import create_db
from shortcut.db.create_table import create_table
from shortcut.db.generate_path import table_obj

if __name__ == '__main__':
    s1 = set(dir(table_obj))
    s2 = set(dir(Post.__class__))
    s2.add('__weakref__')

    columns = list(s1 - s2)

    path = generate_path(columns)

    con, cur = create_db()

    create_table(con, cur, path)

