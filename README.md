# Tawala

Official Tawala SDK and platform connector. Provides secure APIs, data models, and governance-aware mechanisms to exchange AI-related data with the Tawala Platform.

## Description

Tawala is a comprehensive platform for AI governance and risk management. This Python SDK serves as the official client library, enabling developers to programmatically interact with the Tawala platform. It offers secure APIs for managing AI models, systems, risk instances, treatments, and more, ensuring compliance and governance in AI deployments.

Key features include:
- Authentication and secure API access
- Data models for AI-related entities
- Repository classes for CRUD operations on platform resources
- Utility functions for HTTP communication

## Installation

The "pip install tawala" will be soon available, in the meanwhile you can clone and copy this repo.

## Usage

After installation, you can import and use the client:

```python
from tawala import Client

# Initialize the client with your credentials
client = Client(api_key="your-api-key")

# Example: List AI models
models = client.models.list()
```

## Examples

The `examples/` folder contains sample scripts to help you get started with common operations:

- `add_risk_instance.py`: Demonstrates how to create and add a new risk instance to the platform.
- `list_models.py`: Shows how to retrieve and display a list of available AI models.

Run these examples after installing the package to see the SDK in action.

## Next Steps

- **Get Started**: Follow the installation steps above and run the example scripts.
- **API Documentation**: Refer to the docstrings in the source code or visit the official Tawala documentation for detailed API references.
- **Authentication**: Obtain your API key from the Tawala platform dashboard.
- **Contributing**: Report bugs or feature requests on the project's issue tracker.
- **Updates**: Check the CHANGELOG.md for the latest changes and version history.

## License

This project is licensed under the Tawala Custom Source-Available License. See the LICENSE.md file for details.
