def test_signup_success(client):
    # Arrange
    email = "test.student@example.com"
    activity = "Chess Club"
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    res = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert res.status_code == 200
    assert res.json().get("message") == f"Signed up {email} for {activity}"
    assert email in client.get("/activities").json()[activity]["participants"]
