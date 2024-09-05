import requests

def test_frontend_backend_integration():
    # URL of the frontend service
    frontend_url = 'http://localhost:8081'
    
    # Expected message from the backend
    expected_message = 'Hello from the Backend!'
    
    try:
        # Make a request to the frontend service
        response = requests.get(frontend_url)
        
        # Print status code and response text for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Check if the response contains the expected message
        assert expected_message in response.text, "Test failed: Expected message not found!"
        
        print("Test passed: Frontend displays the correct message from the backend.")
        
    except Exception as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    test_frontend_backend_integration()
