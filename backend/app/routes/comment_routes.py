from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import TokenComment
from app.schemas import CommentCreate, TokenComment
from app.crud.comment_crud import create_comment, get_comments_by_token

router = APIRouter()


@router.post("/", response_model=TokenComment)
def create_new_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db, comment)


@router.get("/token/{token_id}", response_model=list[TokenComment])
def read_comments_by_token(token_id: int, db: Session = Depends(get_db)):
    return get_comments_by_token(db, token_id)
