def test_signup_duplicate(client):
    # Arrange
    email = "dup.student@example.com"
    activity = "Programming Class"

    # Ensure first signup succeeds
    res1 = client.post(f"/activities/{activity}/signup?email={email}")
    assert res1.status_code == 200

    # Act: attempt duplicate signup
    res2 = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert res2.status_code == 400
    assert "already signed up" in res2.json().get("detail", "").lower()
