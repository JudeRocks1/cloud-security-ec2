from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, DBLog

# Create tables in PostgreSQL using SQLAlchemy
Base.metadata.create_all(bind=engine)

# Instantiate
app = FastAPI()

# Contract for data entries
class SecurityLog(BaseModel):
    event_id: str
    severity: str

#helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
            db.close()

# POST action with Pydantic validation
@app.post("/ingest")
def ingest(log: SecurityLog, db: Session = Depends(get_db)):
    # Map data to database
    db_record = DBLog(event_id=log.event_id, severity=log.severity)

    #add and commit
    db.add(db_record)
    db.commit()
    #get the id
    db.refresh(db_record)

    return {"status": "saved to database", "internal_id": db_record.id}

# GET action
@app.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    # Returns all logs in the data base
    all_logs = db.query(DBLog).all()
    return all_logs
