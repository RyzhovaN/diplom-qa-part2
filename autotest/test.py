from autotest import api, data


# Надежда Рыжова, 11-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_order():
    # Arrange
    # В переменную track сохраняется трек-номер созданного заказа
    track = api.create_new_order(data.new_order_body)
    # Act
    response = api.get_order(track)
    # Assert
    assert response.status_code == 200



