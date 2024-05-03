from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Bienvenue sur votre API Llama Index !"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601)
import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)

# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ["OPENAI_API_KEY"] = "your key here"

index = None


def initialize_index():
    global index
    storage_context = StorageContext.from_defaults()
    if os.path.exists(index_dir):
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader("./documents").load_data()
        index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
        )
        storage_context.persist(index_dir)


import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)

# NOTE: for local testing only, do NOT deploy with your key hardcoded
os.environ["OPENAI_API_KEY"] = "your key here"

index = None


def initialize_index():
    global index
    storage_context = StorageContext.from_defaults()
    if os.path.exists(index_dir):
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader("./documents").load_data()
        index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
        )
        storage_context.persist(index_dir)


# hhhhhhhhhhhhhhhhhhhhhhhhhhibanokra
