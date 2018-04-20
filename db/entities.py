from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from db.base import Base, inverse_relationship, create_tables 


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String(255))

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref = inverse_relationship('likes'))
    show_id = Column(Integer, ForeignKey('shows.id'))
    show = relationship('Show', backref = inverse_relationship('liked_by'))

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Show(Base):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    tvmaze_id = Column(Integer)
    showname = Column(String)
    show_image_url = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # def parse_dictionary(self, json_data):
    #     self.tvmaze_id = json_data['id']
    #     self.showname = json_data['name']
    #     self.image_url = json_data['medium_image']

if __name__ != '__main__':
    create_tables()