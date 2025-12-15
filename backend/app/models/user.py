from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base
from app.core.roles import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)

    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    role = Column(
        String,
        nullable=False,
        default=UserRole.STAFF.value,
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.role is None:
            self.role = UserRole.STAFF.value
