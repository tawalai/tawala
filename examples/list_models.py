import os
from tawala.client import TawalaClient

def main():
    api_key = os.getenv("TAWALA_API_KEY", "YOUR_API_KEY")
    tawala_host = os.getenv("TAWALA_HOST", "https://platformapi.tawala.ai")
    client = TawalaClient(api_key=api_key, base_url=tawala_host)
    model_list = client.models.list()
    print(model_list)

if __name__ == "__main__":
    main()