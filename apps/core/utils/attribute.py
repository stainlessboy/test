def get_attribute(obj, path: str):
    paths = path.split('.')
    for p in paths:
        obj = getattr(obj, p, None)
    return obj
