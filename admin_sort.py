from sqlalchemy.orm import Session
from db import get_db
from models import AdminData  # Make sure to define this model or replace with your actual admin model

def get_sorted_admin_data(db: Session, sort_by: str = 'id', descending: bool = False):
    sort_column = getattr(AdminData, sort_by)
    if descending:
        return db.query(AdminData).order_by(sort_column.desc()).all()
    else:
        return db.query(AdminData).order_by(sort_column.asc()).all()

# Example usage (inside a FastAPI route or a script):
# with get_db() as db:
#     sorted_data = get_sorted_admin_data(db, sort_by='name', descending=False)
#     for admin in sorted_data:
#         print(admin.name)