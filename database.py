from sqlmodel import SQLModel, create_engine, Field, Session


db_name = "message.db"
db_url = f"sqlite:///{db_name}"

engine = create_engine(db_url, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)
    
class Message(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key= True)
    message : str
create_db_and_table()

def add(message):
    with Session(engine) as session:
        session.add(Message(message=message))
        session.commit()
        return "Message added successfully"
    
def get_all_message():
    with Session(engine) as session:
        messages = session.exec(Message).all()
        return [message.message for message in messages]

def get_by_id():
    with Session (engine) as session:
        messages = session.exec(Message).filter(Message,id).all()
        return messages

def update_message(message):
    with Session(engine) as session:
        messages = session.exec(Message).filter(Message,id).all()
        messages[0].message = message
        session.commit()
        return "Message updated successfully"
    
def delete_message(message):
    with Session (engine) as session:
        session.delete(message)
        session.commit()
        return "Message deleted successfully"
    