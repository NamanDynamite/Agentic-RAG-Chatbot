from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
    CSVLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os


def get_text_splitter():

    return RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=70)


class IngestionAgent:

    def __init__(self):
        self.name = "IngestionAgent"

    def load_docs(self, file_paths):
        docs = []

        for path in file_paths:
            ext = path.split('.')[-1].lower()

            if ext == 'pdf':
                docs.extend(PyPDFLoader(path).load())
            elif ext in ['txt', 'md']:
                docs.extend(TextLoader(path).load())
            elif ext == 'docx':
                docs.extend(UnstructuredWordDocumentLoader(path).load())
            elif ext == 'pptx':
                docs.extend(UnstructuredPowerPointLoader(path).load())
            elif ext == 'csv':
                docs.extend(CSVLoader(path).load())

        return docs

    def handle(self, mcp_msg):
        files = mcp_msg.payload["files"]
        docs = self.load_docs(files)
        splitter = get_text_splitter()
        chunks = splitter.split_documents(docs)

        return {
            "sender": self.name,
            "receiver": "RetrievalAgent",
            "type": "DOC_CHUNKS",
            "trace_id": mcp_msg.trace_id,
            "payload": {"chunks": chunks}
        }