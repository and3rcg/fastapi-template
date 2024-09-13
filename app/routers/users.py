from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session

from ..models.user import User
from ..database import get_session


# tip: if you want to manipulate the request object like Django, you can check out Starlette
# documentation: https://www.starlette.io/requests/

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    return {"message": "User created"}


@router.get("/", status_code=status.HTTP_200_OK)
def list_users(session: Session = Depends(get_session)):
    result = session.query(User).all()
    return result


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def list_users(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# using SQLAlchemy's sessions, you gotta set up the ID manually in the request body 'user_data' and then merge.
# if you don't, it'll create a new user
@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, user_data: User, session: Session = Depends(get_session)):  # Optional[str] == Union[str, None]
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data.id = user_id
    session.merge(user_data)
    session.commit()
    return {"message": "User updated"}


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()
    return

