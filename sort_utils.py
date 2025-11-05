from sqlalchemy.orm import Session
from typing import List, Type
from models import Volunteer, ShopOwner   # Replace or add your AdminData model as needed

def get_sorted_data(db: Session, model: Type, sort_by: str = 'id', descending: bool = False) -> List:
    """Generic sorting utility for any SQLAlchemy model."""
    sort_column = getattr(model, sort_by)
    query = db.query(model).order_by(sort_column.desc() if descending else sort_column.asc())
    return query.all()

def get_sorted_volunteers(db: Session, sort_by: str = 'id', descending: bool = False) -> List[Volunteer]:
    """Sort Volunteer data by any column."""
    return get_sorted_data(db, Volunteer, sort_by, descending)

def get_sorted_users(db: Session, sort_by: str = 'id', descending: bool = False) -> List[ShopOwner]:
    """Sort ShopOwner (User) data by any column."""
    return get_sorted_data(db, ShopOwner, sort_by, descending)

# Example usage:
# with get_db() as db:
#     sorted_volunteers = get_sorted_volunteers(db, sort_by='name')
#     sorted_users = get_sorted_users(db, sort_by='created_at', descending=True)
#     for user in sorted_users:
#         print(user.shop_name)