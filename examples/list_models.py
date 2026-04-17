"""Example script demonstrating how to list AI models.

This example shows how to:
1. Initialize the Tawala client with API credentials
2. Retrieve and display all AI models from the platform

Usage:
    Set TAWALA_API_KEY and optionally TAWALA_HOST environment variables,
    then run: python list_models.py
"""
import os
from tawala import TawalaClient

def main():
    """List all AI models using the Tawala client.
    
    Retrieves the API key and host from environment variables,
    initializes the client, and prints all available models.
    """
    api_key = os.getenv("TAWALA_API_KEY", "YOUR_API_KEY")
    tawala_host = os.getenv("TAWALA_HOST", "https://platformapi.tawala.ai")
    client = TawalaClient(api_key=api_key, base_url=tawala_host)
    model_list = client.models.list()
    print(model_list)

if __name__ == "__main__":
    main()