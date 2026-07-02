def test_get_activities(client):
    # Arrange: client fixture provides TestClient
    # Act
    res = client.get("/activities")

    # Assert
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
