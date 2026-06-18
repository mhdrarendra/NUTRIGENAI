from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()

urlqdrant= os.getenv("QDRANT_URL")
apiqdrant= os.getenv("QDRANT_CLOUD_API")

client = QdrantClient(
    url=urlqdrant,
    api_key=apiqdrant,
)

print(urlqdrant)
print(apiqdrant)
print(client.get_collections())