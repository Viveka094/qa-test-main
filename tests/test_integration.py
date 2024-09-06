import requests
import logging

# Configure logging
logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_frontend_backend_integration():
    # URL of the frontend service
    frontend_url = 'http://localhost:8081'
    
    # Expected message from the backend
    expected_message = 'Hello from the Backend!'
    
    try:
        # Make a request to the frontend service
        response = requests.get(frontend_url)
        
        # Log status code and response text for debugging
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")

        # Check if the response contains the expected message
        assert expected_message in response.text, "Test failed: Expected message not found!"
        logging.info("Test passed: Frontend displays the correct message from the backend.")

        
    except Exception as e:
        logging.error(f"Test failed: {e}")

if __name__ == "__main__":
    test_frontend_backend_integration()
