
def hide_fields(tablename, fields):
    for field in fields:
        db[tablename][field].writable = \
            db[tablename][field].readable = False  