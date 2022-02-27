"""This test the about page"""

def about_test(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
