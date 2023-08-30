def hello_world(name: str) -> str:
    """
    Return greeting based on given name
    """ 
    if not name:
        return "Please introduce yourself :("
    return f"hello {name}"