from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Messages(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(nullable=False)
