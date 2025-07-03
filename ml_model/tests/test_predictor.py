import pytest
from ml_model.predictor import Predictor
import numpy as np

def test_model_predicts_correctly():
    predictor = Predictor()
    input_data = np.zeros(21)
    output = predictor.predict(input_data)
    assert output in [1, 2, 3]

def test_model_invalid_input():
    predictor = Predictor()
    with pytest.raises(ValueError):
        predictor.predict(np.zeros(10))
