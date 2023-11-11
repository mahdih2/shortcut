from shortcut.db.models import models

class Post:
    id = models.integer_field()
    title = models.char_field()
    
