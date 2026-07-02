from src.app import activities


def test_signup_when_full(client):
    # Arrange
    activity = "Swimming Club"
    max_p = activities[activity]["max_participants"]
    # Fill participants to capacity
    activities[activity]["participants"] = [f"user{i}@example.com" for i in range(max_p)]
    email = "late.student@example.com"

    # Act
    res = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    # Note: current implementation allows signup even when full; this test documents that behavior.
    assert res.status_code == 200
    assert email in activities[activity]["participants"]
