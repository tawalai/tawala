from tawala.client import TawalaClient

def main():
    client = TawalaClient("YOUR_API_KEY")
    messages = client.models.list()
    print(messages)

if __name__ == "__main__":
    main()