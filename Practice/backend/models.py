from app import db

class Friend(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    role=db.Column(db.String(50),nullable=False)
    decription=db.Column(db.Text,nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    img_urL=db.Column(db.String(200),nullable=False)
    
    def to_JSON(self):
        
        return {
            "id" : self.id,
            "name" : self.name,
            "role" : self.role,
            "description" : self.description,
            "gender" : self.gender,
            "img_urL" : self.img_urL
        }