from . import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.save()

    def __init__(self, title:str, description:str, completed:bool):
        self.title = title
        self.description = description
        self.completed = completed
        self.save()

    def __str__(self):
        return f"{self.id} | {self.title} | {self.description} | {self.completed} | {self.created_at}"

    # When creating a new Task, it will be added to our database
    def save(self):
        db.session.add(self)
        db.session.commit()



