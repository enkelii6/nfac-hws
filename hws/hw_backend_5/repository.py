from typing import List, Dict, Optional
import uuid


class UserRepository:
    def __init__(self):
        self.users: List[Dict] = []

    def create_user(self, email: str, full_name: str, password: str, photo_path: Optional[str] = None) -> Dict:
        user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "full_name": full_name,
            "password": password,
            "photo_path": photo_path
        }
        self.users.append(user)
        return user

    def get_user_by_email(self, email: str) -> Optional[Dict]:
        return next((u for u in self.users if u["email"] == email), None)

    def get_user_by_id(self, user_id: str) -> Optional[Dict]:
        return next((u for u in self.users if u["id"] == user_id), None)


class FlowerRepository:
    def __init__(self):
        self.flowers: List[Dict] = []
        self.next_id = 1

    def add_flower(self, name: str, count: int, cost: float) -> Dict:
        flower = {
            "id": self.next_id,
            "name": name,
            "count": count,
            "cost": cost
        }
        self.flowers.append(flower)
        self.next_id += 1
        return flower

    def get_flower_by_id(self, flower_id: int) -> Optional[Dict]:
        return next((f for f in self.flowers if f["id"] == flower_id), None)

    def get_all_flowers(self) -> List[Dict]:
        return self.flowers


class PurchaseRepository:
    def __init__(self):
        self.purchases: List[Dict] = []

    def add_purchase(self, user_id: str, flower_id: int) -> Dict:
        purchase = {
            "user_id": user_id,
            "flower_id": flower_id
        }
        self.purchases.append(purchase)
        return purchase

    def get_user_purchases(self, user_id: str) -> List[Dict]:
        return [p for p in self.purchases if p["user_id"] == user_id]


user_repo = UserRepository()
flower_repo = FlowerRepository()
purchase_repo = PurchaseRepository()