from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):

    __tablename__ = 'blogs'
  

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    # NOVA COLUNA DB
    user_id = Column(Integer, ForeignKey("users.id"))
    # VARIAVEL PARA UTILIZAR NAS DEMAIS CLASSES
    creator = relationship('User', back_populates='blogs')

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    # VARIAVEL PARA UTILIZAR NAS DEMAIS CLASSES
    blogs = relationship('Blog', back_populates='creator')

