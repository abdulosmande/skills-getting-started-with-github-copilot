def test_delete_participant(client):
    # Arrange
    email = "remove.me@example.com"
    activity = "Gym Class"

    # Add participant first
    add_res = client.post(f"/activities/{activity}/signup?email={email}")
    assert add_res.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act: remove participant
    res = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert res.status_code == 200
    assert "Removed" in res.json().get("message", "")
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act: remove non-existent participant
    res2 = client.delete(f"/activities/{activity}/participants?email=nonexistent@example.com")
    assert res2.status_code == 404
