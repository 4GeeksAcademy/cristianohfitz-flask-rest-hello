from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class user(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(15), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    caption: Mapped[str] = mapped_column(String(150), unique=True)
    img: Mapped[str] = mapped_column(String(50), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)

class comment(db.Model):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(150), unique=True)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False) 

class like(db.Model):
    __tablename__ = "like"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False) 

class story(db.Model):
    __tablename__ = "story"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)

class share(db.Model):
    __tablename__ = "share"
    id: Mapped[int] = mapped_column(primary_key=True)
    story_ID: Mapped[int] = mapped_column(ForeignKey("Story.id"), nullable=False)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    text: Mapped[str] = mapped_column(String(30))
