from sqlalchemy.orm import Session
from models import Volunteer, ShopOwner

def get_all_volunteers(db: Session):
    return db.query(Volunteer).all()

def get_all_users(db: Session):
    return db.query(ShopOwner).all()

# Python's built-in sort (Timsort)
def sort_records(records, sort_by="id", descending=False):
    return sorted(records, key=lambda x: getattr(x, sort_by), reverse=descending)

# Example of Bubble Sort (not efficient for large datasets; for learning purposes)
def bubble_sort_records(records, sort_by="id", descending=False):
    n = len(records)
    for i in range(n):
        for j in range(0, n-i-1):
            a = getattr(records[j], sort_by)
            b = getattr(records[j+1], sort_by)
            if (a > b and not descending) or (a < b and descending):
                records[j], records[j+1] = records[j+1], records[j]
    return records

# Usage example:
def example_usage(db: Session):
    volunteers = get_all_volunteers(db)
    users = get_all_users(db)

    sorted_volunteers = sort_records(volunteers, sort_by="name")  # ascending by name
    sorted_users = bubble_sort_records(users, sort_by="created_at", descending=True)  # descending by created_at

    print("Sorted Volunteers:")
    for v in sorted_volunteers:
        print(v.name)
    print("Sorted Users by Created At (Descending):")
    for u in sorted_users:
        print(u.shop_name, u.created_at)