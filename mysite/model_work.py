import joblib
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def model_load(name):
    """
    Возвращает ссылку на импортированную модель
    """
    
    return joblib.load(name)

def model_answer(model, reveiw):
    """
    Возвращаетт рейтинг, спрогнозированный моделью и 
    эмоциональную окраску на основе предсказанного рейтинга
    """
    rate = model.predict(reveiw)
    sentiment_bin = 1 if rate > 5 else 0

    return rate, sentiment_bin