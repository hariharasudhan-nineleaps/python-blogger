import uuid

def generate_unique_id() -> str:
    return uuid.uuid4().hex