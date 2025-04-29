import pytest
from httpx import AsyncClient

# Import your FastAPI app instance
# Assuming your app instance in app/main.py is named 'app'
from app.main import app 

@pytest.mark.asyncio
async def test_read_docs():
    """Test if the /docs endpoint returns 200 OK."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/docs")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_main():
    """Test if the root endpoint returns 404 Not Found (assuming no default route)."""
    # Adjust the expected status code if you have a route defined for "/"
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 404 # Or 200 if you have a root route 