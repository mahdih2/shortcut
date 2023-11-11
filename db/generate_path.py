from shortcut.app.models import Post

table_obj = Post()

def generate_path(columns):
    values = []
    for i in columns:
        values.append(table_obj.__class__.__dict__[i])
    path = f"CREATE TABLE {table_obj.__class__.__name__}("
    for i, j in enumerate(columns):
        path += f"{j} {values[i]}"
        if i < len(values)-1:
            path += ", "
    path += ")"
    return path