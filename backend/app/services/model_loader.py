import os
import pickle
from pathlib import Path

class ModelLoader:
    def __init__(self, model_path: str):
        self.model_path = Path(model_path)
        self.model = None
        self.cache = {}

    def load_model(self):
        if self.model is None:
            if self.model_path.exists():
                with open(self.model_path, 'rb') as f:
                    self.model = pickle.load(f)
            else:
                raise FileNotFoundError(f'No model found at {self.model_path}')
        return self.model

    def cache_model(self):
        if self.model is not None:
            self.cache[self.model_path.name] = self.model

    def get_cached_model(self, model_name: str):
        return self.cache.get(model_name, None)

# Example Usage
# loader = ModelLoader('path/to/your/model.pkl')
# model = loader.load_model()
# loader.cache_model()  
# cached_model = loader.get_cached_model('model.pkl')
