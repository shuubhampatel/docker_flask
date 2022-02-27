def test_request_example(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
