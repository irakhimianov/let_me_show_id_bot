from datetime import datetime

from sqlalchemy import Column, BigInteger, Boolean, DateTime

from database import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'<User: {self.user_id} {self.is_active=} {self.created_at=:%d-%m-%Y %H:%M}>'
