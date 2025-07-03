import pickle

class Predictor:
    def __init__(self, model_path='model_at.sav'):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, features):
        return self.model.predict([features])[0]
