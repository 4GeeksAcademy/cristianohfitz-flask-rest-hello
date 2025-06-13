from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    __tablename__ = "Post"
    id: Mapped[int] = mapped_column(primary_key=True)
    caption: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    img: Mapped[str] = mapped_column(String(50), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)

class Comment(db.Model):
    __tablename__ = "Comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False) 

class Like(db.Model):
    __tablename__ = "Like"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False) 

class Story(db.Model):
    __tablename__ = "Story"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    user_ID: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)

class Share(db.Model):
    __tablename__ = "Share"
    id: Mapped[int] = mapped_column(primary_key=True)
    story_ID: Mapped[int] = mapped_column(ForeignKey("Story.id"), nullable=False)
    post_ID: Mapped[int] = mapped_column(ForeignKey("Post.id"), nullable=False)
    text: Mapped[str] = mapped_column(String(30))
