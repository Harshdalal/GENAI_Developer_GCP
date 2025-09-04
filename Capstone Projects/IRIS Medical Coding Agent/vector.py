from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings, DEFAULT_TENANT
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

class MedicalVectorStore:
    """
    A class to manage the vector store for medical documents using ChromaDB.
    
    This class handles the creation and storage of vector embeddings
    for EHR records organized by clinical specialties or conditions.
    
    IMPORTANT:
    - All metadata must be properly processed for ChromaDB compatibility
    - This implementation uses OpenAI embeddings with the "text-embedding-3-small" model
    - The class expects directories and permissions to be properly set up for persistent storage
    """
    
    def __init__(self, vecstore_path: str):
        """
        Initialize the vector store with ChromaDB client and OpenAI embeddings.
        
        Args:
            vecstore_path (str): Path where ChromaDB will persist vector store data
            
        Raises:
            ValueError: If OPENAI_API_KEY environment variable is not set
        """
        self.vecstore_path = vecstore_path
        self.client = chromadb.PersistentClient(path=self.vecstore_path, tenant=DEFAULT_TENANT)
        
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
            
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_api_key)
        self.collections = {}
    
    def prepare_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare metadata for ChromaDB by converting lists to strings and ensuring valid types.
        
        ChromaDB requires all metadata values to be primitive types (str, int, float, bool).
        Lists must be converted to comma-separated strings, and None values must be handled.
        
        Args:
            metadata (Dict[str, Any]): Original metadata dictionary
            
        Returns:
            Dict[str, Any]: Processed metadata with ChromaDB-compatible types
        """
        processed = {}
        for key, value in metadata.items():
            if isinstance(value, list):
                # Convert lists to comma-separated strings
                processed[key] = ','.join(str(item) for item in value) if value else ''
            elif isinstance(value, (str, int, float, bool)) or value is None:
                # Keep valid primitive types, convert None to empty string
                processed[key] = value if value is not None else ''
            else:
                # Convert any other types to strings
                processed[key] = str(value)
        return processed
    
    def create_vector_store(self, documents: List[Document], collection_name: str = "medical_records") -> None:
        """
        Create a vector store collection from documents.
        
        Args:
            documents (List[Document]): List of documents to add to the collection
            collection_name (str): Name of the collection to create
        """
        # Create or get collection
        collection = self.client.create_collection(
            name=collection_name,
            metadata={"collection_name": collection_name}
        )
        
        # Prepare documents for insertion
        ids = []
        for i, doc in enumerate(documents):
            # Use row_id if available, otherwise use index
            if 'row_id' in doc.metadata:
                ids.append(str(doc.metadata['row_id']))
            elif 'SUBJECT_ID' in doc.metadata:
                ids.append(str(doc.metadata['SUBJECT_ID']))
            else:
                ids.append(f"doc_{i}")
                
        texts = [doc.page_content for doc in documents]
        metadatas = [self.prepare_metadata(doc.metadata) for doc in documents]
        
        # Generate embeddings and add to collection
        embeddings = self.embeddings.embed_documents(texts)
        
        collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=texts
        )
        
        self.collections[collection_name] = collection
    
    @classmethod
    def load_local(cls, directory: str) -> 'MedicalVectorStore':
        """
        Load a vector store from local storage.
        
        Args:
            directory (str): Directory path containing the vector store
            
        Returns:
            MedicalVectorStore: Loaded vector store instance or None if no collections found
        """
        # Create new instance with the directory
        instance = cls(vecstore_path=directory)
        
        # Load all collections
        collections = instance.client.list_collections()
        for collection in collections:
            collection_obj = instance.client.get_collection(collection.name)
            metadata = collection.metadata or {}
            collection_name = metadata.get('collection_name')
            if collection_name:
                instance.collections[collection_name] = collection_obj
        if instance.collections:
            return instance
        else:
            return None
    
    def get_collection_names(self) -> List[str]:
        """
        Get list of available collection names in the vector store.
        
        Returns:
            List[str]: List of collection names
        """
        return list(self.collections.keys())