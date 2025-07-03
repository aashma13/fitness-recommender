import pandas as pd
from datasets import Dataset
import os

class ObjectCache:
    def __init__(self):
        self.cached_object = None

    def load_object(self):
        """
        Loads the object from the local cache path into memory.
        """
        df = pd.read_pickle('fitness_data_embedding.pickle')
        search_df = df[['uid', 'content', 'embeddings']]
        
        # Cache the dataset in memory with a FAISS index
        self.cached_object = Dataset.from_pandas(search_df)
        self.cached_object.add_faiss_index(column="embeddings")
        
        print("Object loaded into memory.")

    def get_object(self):
        """
        Returns the cached object, reloading it if necessary.
        """
        if self.cached_object is None:
            print("Cached object is None, attempting to re-download and load...")
            self.load_object()
        return self.cached_object
