import pytest
from fastapi import status
from sqlalchemy import select

from src.models import books, sellers


# Тест на ручку создающую продавца
@pytest.mark.asyncio
async def test_create_seller(async_client):
    data = {"first_name": "Sel", "last_name": "Seller", "email": "sel@seller.com", "password": "selseller"}

    response = await async_client.post("/api/v1/sellers/", json=data)

    assert response.status_code == status.HTTP_201_CREATED

    result_data = response.json()

    assert result_data == {
        "id": response.json()["id"],
        "first_name": "Sel",
        "last_name": "Seller",
        "email": "sel@seller.com",
    }


# Тест на ручку получения списка продавцов
@pytest.mark.asyncio
async def test_get_sellers(db_session, async_client):
    seller_1 = sellers.Seller(first_name="Sel", last_name="Seller", email="sel@seller.com", password="selseller")
    seller_2 = sellers.Seller(first_name="Sel2", last_name="Seller2", email="sel2@seller.com", password="selseller2")

    db_session.add_all([seller_1, seller_2])
    await db_session.flush()

    response = await async_client.get("/api/v1/sellers/")

    assert response.status_code == status.HTTP_200_OK

    # Проверяем интерфейс ответа, на который у нас есть контракт.
    assert response.json() == {
        "sellers": [
            {"first_name": "Sel", "last_name": "Seller", "email": "sel@seller.com", "id": seller_1.id},
            {"first_name": "Sel2", "last_name": "Seller2", "email": "sel2@seller.com", "id": seller_2.id},
        ]
    }


# Тест на ручку получения одного продавца
@pytest.mark.asyncio
async def test_get_single_seller(db_session, async_client):
    # Создаем продавцов вручную, а не через ручку, чтобы нам не попасться на ошибку которая
    # может случиться в POST ручке
    seller_1 = sellers.Seller(first_name="Sel", last_name="Seller", email="sel@seller.com", password="selseller")
    seller_2 = sellers.Seller(first_name="Sel2", last_name="Seller2", email="sel2@seller.com", password="selseller2")
    db_session.add_all([seller_1, seller_2])
    await db_session.flush()

    book = books.Book(author="Pushkin", title="Eugeny Onegin", year=2001, count_pages=104, seller_id=seller_1.id)
    book_2 = books.Book(author="Lermontov", title="Mziri", year=1997, count_pages=104, seller_id=seller_2.id)

    db_session.add_all([book, book_2])
    await db_session.flush()

    response = await async_client.get(f"/api/v1/sellers/{seller_1.id}")

    assert response.status_code == status.HTTP_200_OK

    # Проверяем интерфейс ответа, на который у нас есть контракт.
    assert response.json() == {
        "id": seller_1.id,
        "first_name": "Sel",
        "last_name": "Seller",
        "email": "sel@seller.com",
        "books": [{"author": "Pushkin", "title": "Eugeny Onegin", "year": 2001, "count_pages": 104, "id": book.id}],
    }


# Тест на ручку удаления продавца
@pytest.mark.asyncio
async def test_delete_seller(db_session, async_client):
    # Создаем продавца вручную, а не через ручку, чтобы нам не попасться на ошибку которая
    # может случиться в POST ручке
    seller_1 = sellers.Seller(first_name="Sel", last_name="Seller", email="sel@seller.com", password="selseller")

    db_session.add(seller_1)
    await db_session.flush()

    response = await async_client.delete(f"/api/v1/sellers/{seller_1.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    await db_session.flush()

    all_sellers = await db_session.execute(select(sellers.Seller))
    res = all_sellers.scalars().all()
    assert len(res) == 0


# Тест на ручку обновления продавца
@pytest.mark.asyncio
async def test_update_seller(db_session, async_client):
    # Создаем продавца вручную, а не через ручку, чтобы нам не попасться на ошибку которая
    # может случиться в POST ручке
    seller_1 = sellers.Seller(first_name="Sel", last_name="Seller", email="sel@seller.com", password="selseller")

    db_session.add(seller_1)
    await db_session.flush()

    response = await async_client.put(
        f"/api/v1/sellers/{seller_1.id}",
        json={"first_name": "Shylock", "last_name": "Shakespeare", "email": "shylock@shakespeare.com", "password": "dddfggh"},
    )

    assert response.status_code == status.HTTP_200_OK
    await db_session.flush()

    # Проверяем, что обновились все поля
    res = await db_session.get(sellers.Seller, seller_1.id)
    assert res.first_name == "Shylock"
    assert res.last_name == "Shakespeare"
    assert res.email == "shylock@shakespeare.com"
    assert res.password == "dddfggh"
    assert res.id == seller_1.id
