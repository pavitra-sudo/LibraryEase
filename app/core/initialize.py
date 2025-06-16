from app.core.database import Base, engine

def initialize_database():
    from app.models import user
    Base.metadata.create_all(bind=engine)
