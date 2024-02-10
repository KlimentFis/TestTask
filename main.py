from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI()

# Пример базы данных для справочника
fake_db = [
    {"name": "Иван", "phone": "1234567890", "email": "ivan@example.com"},
    {"name": "Мария", "phone": "0987654321", "email": "maria@example.com"}
]

@app.get('/')
def index():
    return 'Перейдите на страницу contacts !!!'

# Функция для постраничного вывода записей
def paginate_results(results: List[dict], page: int, page_size: int):
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return results[start_idx:end_idx]

# Получить все записи в справочнике
@app.get("/contacts/", response_model=List[dict])
async def get_contacts(page: int = 1, page_size: int = 10):
    return paginate_results(fake_db, page, page_size)

# Добавить новую запись в справочник
@app.post("/contacts/", status_code=201)
async def add_contact(name: str, phone: str, email: Optional[str] = None):
    new_contact = {"name": name, "phone": phone, "email": email}
    fake_db.append(new_contact)
    return {"message": "Contact added successfully"}

# Редактировать запись в справочнике
@app.put("/contacts/{contact_id}/", status_code=200)
async def update_contact(contact_id: int, name: str, phone: str, email: Optional[str] = None):
    if contact_id < 0 or contact_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Contact not found")
    fake_db[contact_id] = {"name": name, "phone": phone, "email": email}
    return {"message": "Contact updated successfully"}

# Поиск записей по характеристикам
@app.get("/contacts/search/", response_model=List[dict])
async def search_contacts(name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None):
    results = fake_db
    if name:
        results = [contact for contact in results if contact["name"] == name]
    if phone:
        results = [contact for contact in results if contact["phone"] == phone]
    if email:
        results = [contact for contact in results if contact["email"] == email]
    return results
