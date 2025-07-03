import requests

def test_post_exame():
    url = 'http://localhost:8000/registros'
    payload = {
        "cpf": "12345678900",
        "baseline_value": 120,
        "accelerations": 0.003,
        "fetal_movement": 0.01,
        "uterine_contractions": 0.0,
        "light_decelerations": 0.0,
        "severe_decelerations": 0.0,
        "prolongued_decelerations": 0.0,
        "abnormal_short_term_variability": 0.0,
        "mean_value_of_short_term_variability": 0.8,
        "percentage_of_time_with_abnormal_long_term_variability": 0.0,
        "mean_value_of_long_term_variability": 1.2,
        "histogram_width": 50,
        "histogram_min": 70,
        "histogram_max": 150,
        "histogram_number_of_peaks": 5,
        "histogram_number_of_zeroes": 0,
        "histogram_mode": 120,
        "histogram_mean": 125,
        "histogram_median": 124,
        "histogram_variance": 30,
        "histogram_tendency": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert 'fetalhealth' in response.json()
